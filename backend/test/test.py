import json

context = {"dataset": "iris.csv", "lr": 0.0001, "test_batch_size": 32, "batch_size": 64, "epoch": 20, "seed": 1}

with open("hyper.json", 'w') as f:
    json.dump(context, f)
