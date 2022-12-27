# 다중 퍼셉트론으로 손글씨 분류
# 사이킷런에있는 제공된 이미지 이용

import matplotlib.pyplot as plt

import torch
import torch.nn as nn
from torch import optim

from sklearn.datasets import load_digits


digits = load_digits()

# 첫번째 샘플 출력 .images[인덱스] 8x8
print(digits.images[1])

# 실제 레이블도 숫자 0인지 첫번째 샘플레이어 확인
print(digits.target[1])

# 전체 이미지 개수 : 1797
print('전체이미지 수 : ', len(digits.images))

# enumerate() , zip() 많이 씀
# 상위 5개만 샘플이미지를 확인 _ zip() : 각각 나오는 이미지와 타겟을 묶음
'''
image = [1,2,3,4]
label = [사과, 바나나, 자몽, 수박]
이미지와 라벨 리스트 길이 동일하므로 zip() 사용할수있음
1 사과 2 바나나 3 자몽 4 수박
'''

# image와 label 뽑아서 묶어놓기
image_and_label_list = list(zip(digits.images, digits.target))

# 위에서 묶어놓은것중 4개의 샘플만 보기
for index, (image, label) in enumerate(image_and_label_list[:4]):
    plt.subplot(2,5, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap = plt.cm.gray_r, interpolation = 'nearest')
    plt.title('sample: %i' % label)
plt.show()

# 상위 레이블 5개 확인
for i in range(5):
    print(i, '번 index sample label:',digits.target[i])


# train data and label
x = digits.data  # 이미지 데이터
y = digits.target # 각 이미지 레이블

model = nn.Sequential(
    nn.Linear(64, 32), # input_layer = 64 hidden_layer_1 = 32
    nn.ReLU(), # 여기서 활성화함수는 Relu 써주기
    nn.Linear(32, 16), # input_layer = 32 hidden_layer_2 = 16
    nn.ReLU(),
    nn.Linear(16, 10) # input_layer = 16 hidden_layer_2 = 10
    # output이 10 이므로 CrossEntropyLoss() 써야한다. 
    # CrossEntropyLoss() : output layer = 2 이상인경우 사용
    # BCELoss() : output layer = 1 인경우사용

)

print(model)
 
'''
Sequential(
  (0): Linear(in_features=64, out_features=32, bias=True)
  (1): ReLU()
  (2): Linear(in_features=32, out_features=16, bias=True)
  (3): ReLU()
  (4): Linear(in_features=16, out_features=10, bias=True)
)'''

# x, y를 tensor로 바꿔주기
x = torch.tensor(x, dtype=torch.float32)
y = torch.tensor(y, dtype=torch.int64)


loss_fun = nn.CrossEntropyLoss() # 소프트 맥스 함수를 포함
optimizer = optim.Adam(model.parameters())

losses = []  # loss 그래프 확인
epoch_number = 100

##이 에포크 돌리는 구조 잘 알아두기##
for epoch in range(epoch_number+1):
    output=model(x)
    loss=loss_fun(output, y)
    
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print('Epoch : [{:4d}/{}] loss : {:6f}'.format(epoch, 
             epoch_number, loss.item()))

    # append : losses 리스트에 하나씩 append하기위함
    losses.append(loss.item())

plt.title('loss')
plt.plot(losses)
plt.show()






