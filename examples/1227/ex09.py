# 파이토치로 다층 퍼셉트론 구현
import torch
import torch.nn as nn

# step 1. GPU 사용 가능한지 여부 파악 (-안되면 cpu 동작해야되기때문)
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(device)

# xor 문제를 풀기 위한 입력과 출력 정
x = [[0,0], [0,1], [1,0], [1,1]]
y = [[0], [1], [1], [0]]

x = torch.tensor(x, dtype=torch.float32).to(device)
y = torch.tensor(y, dtype = torch.float32).to(device)


# 총 은닉층 3개인 신경망 구성하기
# 참고 : crossEntropy 경우엔 마지막 레이어 노드수가 2개이상이어야 한다.

 

### model 선언해주기 ###

# 입력층, 은닉층1, 은닉층2, 은닉층3, 출력층 <- 모델 구조

model = nn.Sequential(
    
    # input layer = 2, 첫번째 hidden layer1 = 10
    nn.Linear(2, 10, bias = True), 
    nn.Sigmoid(),
    
    # hidden layer1 = 10, hidden layer2 = 10
    nn.Linear(10, 10, bias = True), 
    nn.Sigmoid(),
 
    # hidden layer2 = 10, hidden layer3 = 10
    nn.Linear(10, 10, bias = True), 
    nn.Sigmoid(),
    
    # hidden layer3 = 10, output layer = 1
    nn.Linear(10, 1, bias = True), 
    nn.Sigmoid() # 우리가 사용할 loss BCELoss 이므로 마지막 레이어를 시그모이드 함수 적용
).to(device)

print(model)
 



# loss 설정하기
criterion = torch.nn.BCELoss()
# optimizer 설정하기
optimizer = torch.optim.SGD(model.parameters(), lr = 0.1) # loss값을 빨리 떨어뜨리고싶으면 lr 조절하기(올리기)

# 10000번 에포크 수행하겠습니다
epoch_number = 45000
for epoch in range(epoch_number + 1):
    output = model(x) # -> 예측된 값

    loss = criterion(output, y) # 예측과 정답지 제공
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 100의배수에 해당되는 에포크마다 loss print
    # loss 는 tensor이므로 item으로 처리
    if epoch % 100 == 0:
        print(f'Epoch : {epoch} : loss : {loss.item()}')


# 인퍼런스 코드
with torch.no_grad():
    output = model(x)
    predicted = (output > 0.5).float()
    acc = (predicted == y).float().mean()
    print('모델의 출력값 /n output', output.detach().cpu().numpy())
    print('모델의 예측값 /n output', predicted.detach().cpu().numpy())
    print('실제값(Y) ', y.cpu().numpy())
    print('정확도 -> ', acc.item())

    # 실제값 0, 1, 1, 0

'''
모델의 출력값 output [[0.500061  ]
 [0.50018406]
 [0.49981958]
 [0.49992764]]
모델의 예측값 output [[1.]
 [1.]
 [0.]
 [0.]]
실제값(Y)  [[0.]
 [1.]
 [1.]
 [0.]]
정확도 ->  0.5'''                                                                                                                                                                                                                                                                                                                                                                                                   




