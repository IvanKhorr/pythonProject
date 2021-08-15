def predict(pred_val):
    if pred_val == 1:
        answ = 'OK'
    elif pred_val == 0:
        answ = 'NO'
    else:
        answ = 'HZ'
    return answ

print (predict(1))