import qrcode
with open('site_list.txt', 'rt', encoding = 'UTF8') as f:    # 이제부턴 이 파일의이름이 f가 된다는뜻
                                                             # with open = 파일의 범위가 잡힘, 즉 알아서 블럭단위(범위를) 닫아줌
    read_lines = f.readlines()      # 전체라인을 읽어옴

    for line in read_lines:         # 전체라인에있는것들을 한개씩 이 for문에 넣어줌, 그리고 하나씩 차례대로 마지막까지 읽음
        line = line.strip()         # strip() : 글자이외의것을 발라냄. 
        print(line)

        qr_data = line
        qr_image = qrcode.make(qr_data)

        qr_image.save(qr_data + '.png')

