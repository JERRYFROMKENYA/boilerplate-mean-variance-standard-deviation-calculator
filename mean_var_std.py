import numpy as np

def calculate(list):
    np.set_printoptions(precision=16)

    if len(list)==9:
        x=np.array(list,dtype='float')
        
        nnp=x.reshape(3,3)
                
        calculations={
                'mean': [nnp.mean(axis=0).tolist(), nnp.mean(axis=1).tolist(), nnp.mean().tolist()],
                'variance': [nnp.var(axis=0).tolist(), nnp.var(axis=1).tolist(), nnp.var().tolist()],
                'standard deviation': [nnp.std(axis=0).tolist(), nnp.std(axis=1).tolist(), nnp.std().tolist()],
                'max': [nnp.max(axis=0).tolist(), nnp.max(axis=1).tolist(), nnp.max().tolist()],
                'min': [nnp.min(axis=0).tolist(), nnp.min(axis=1).tolist(), nnp.min().tolist()],
                'sum': [nnp.sum(axis=0).tolist(), nnp.sum(axis=1).tolist(), nnp.sum().tolist()]
                    }
        return calculations
    else:
        raise ValueError("List must contain nine numbers.")