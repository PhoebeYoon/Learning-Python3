#for ���� Ȱ���� ����, ��� ���ϱ� �鿩���� ����
Scores = [[92, 80, 87], [94, 82, 86], [74, 65, 69], [87, 89, 81], [67, 65, 74]]

for row in Scores:
    total =0
    for col in row: 
      total = total+col
      
    average = total/len(row)
    print(format(average, ".2f"))