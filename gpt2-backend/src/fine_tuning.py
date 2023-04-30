from datasets import load_dataset
from transformers import GPT2Tokenizer, Trainer, GPT2LMHeadModel, TrainingArguments

class GPT2Trainer(Trainer):
    def compute_loss(self, model, inputs, return_outputs=False):
        labels = inputs.pop("labels")
        outputs = model(**inputs, labels=labels)
        loss = outputs.loss
        return (loss, outputs) if return_outputs else loss

def tokenize_function(examples):
    tokens = tokenizer(examples["text"], truncation=True, max_length=128, padding="max_length")
    tokens["labels"] = tokens["input_ids"].copy()
    return tokens

if __name__ == "__main__":
    # Load the tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token
    
    # Load the dataset
    train_dataset = load_dataset("text", data_files={"train": "../datasets/data.txt"})["train"]
    tokenized_train_dataset = train_dataset.map(tokenize_function, batched=True, num_proc=1, remove_columns=["text"])

    # Fine-tune the model
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    model.config.pad_token_id = model.config.eos_token_id

    # Training arguments
    training_args = TrainingArguments(
        output_dir="../trainer_output",
        overwrite_output_dir=True,
        num_train_epochs=1,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
        logging_steps=100,
    )

    # Trainer
    trainer = GPT2Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_train_dataset,
    )

    # Train and save
    trainer.train()
    trainer.save_model("fine_tuned_gpt2")
    tokenizer.save_pretrained("fine_tuned_gpt2")
