python run_mlm.py \
    --model_name_or_path bert-base-uncased \
    --line_by_line \
    --train_file ../../data/fine_tune_train_strings.txt \
    --per_device_train_batch_size 8 \
    --per_device_eval_batch_size 8 \
    --do_train \
    --output_dir bert_fine_tuned