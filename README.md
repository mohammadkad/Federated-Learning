### Federated-Learning

## Frameworks:
- Flower: https://flower.ai/
  - Strategy: https://flower.ai/docs/framework/ref-api/flwr.server.strategy.html
- PySyft: https://github.com/OpenMined/PySyft
- FedML: https://github.com/FedML-AI/FedML
- FATE: https://github.com/FederatedAI/FATE
- openfederatedlearning: https://github.com/securefederatedai/openfederatedlearning
- FedLab: https://github.com/SMILELab-FL/FedLab

## Benchmark:
- leaf: https://github.com/TalwalkarLab/leaf

<!-- 1404-07-19 -->
### Federated Learning:
- Federated learning is a machine learning technique that trains a model collaboratively across multiple devices without centralizing sensitive data.

### Cases:
- data is not available on a centralized server
- data available on one server is not enough to train a good model
- Regulations
- User preference
- Data volume
- Privacy

### Compare:
- Centralized machine learning: move the data to the computation
- Federated (machine) Learning: move the computation to the data

### Federated learning in five steps:
- Step 0: Initialize global model
- Step 1: Send model to a number of connected organizations/devices (client nodes)
- Step 2: Train model locally on the data of each organization/device (client node)
- Step 3: Return model updates back to the server
- Step 4: Aggregate model updates into a new global model
  - Federated Averaging (McMahan et al., 2016), often abbreviated as FedAvg
- Step 5: Repeat steps 1 to 4 until the model converges

### cross-silo
- We simulate having multiple datasets from multiple organizations (also called the “cross-silo” setting in federated learning) by splitting the original CIFAR-10 dataset into multiple partitions.

### Flower:
- Federated Learning with PyTorch and Flower (Quickstart Example):
  - https://github.com/adap/flower/tree/main/examples/quickstart-pytorch

- Install Flower:
  - pip install flwr
  - pip install "flwr[simulation]"
  - import flwr
  - print(flwr.__version__) # 1.22.0

- flwr new flower-tutorial --framework pytorch --username flwrlabs
- cd flower-tutorial
- pip install -e .
- flwr run . OR flwr run . --run-config "num-server-rounds=5 local-epochs=3"

- New: <!-- 1404-10-08 -->
- pip install -U "flwr[simulation]"
- flwr new @flwrlabs/quickstart-pytorch
- cd quickstart-pytorch
- pip install -e .
- flwr run .

#### baselines: https://github.com/adap/flower/tree/main/baselines
- https://flower.ai/docs/baselines/
- FedProx: Federated Optimization in Heterogeneous Networks, https://flower.ai/docs/framework/ref-api/flwr.server.strategy.FedProx.html
-  

#### Datasets:
- FEMNIST (Federated Extended MNIST), extends MNIST to letters + digits.

#### Encryption:
- Homomorphic Encryption (HE)

### PySyft:


## Others:
- Incentive-Based Federated Learning


