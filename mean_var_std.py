import numpy as np

def calculate(list):

 if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
 else:
    a=np.array(list)
    b=np.reshape(a,(3,3))
    m = [np.mean(b, axis=0).tolist(), np.mean(b, axis=1).tolist(), np.mean(a).tolist()]
    v = [np.var(b, axis=0).tolist(), np.var(b, axis=1).tolist(), np.var(a).tolist()]
    s = [np.std(b, axis=0).tolist(), np.std(b, axis=1).tolist(), np.std(a).tolist()]
    ma = [np.max(b, axis=0).tolist(), np.max(b, axis=1).tolist(), np.max(a).tolist()]
    mi = [np.min(b, axis=0).tolist(), np.min(b, axis=1).tolist(), np.min(a).tolist()]
    su = [np.sum(b, axis=0).tolist(), np.sum(b, axis=1).tolist(), np.sum(a).tolist()]
    calculations={'mean':m,
                  'variance':v,
                  'standard deviation':s,
                  'max':ma,
                  'min':mi,
                  'sum':su}
    

    return calculations