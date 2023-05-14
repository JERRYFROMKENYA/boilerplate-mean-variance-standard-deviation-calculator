import numpy as np

def calculate(list):
    np.set_printoptions(precision=16)

    if len(list)==9:
        x=np.array(list,dtype='float')
        
        nnp=x.reshape(3,3)
                
        calculations={
                'mean': [nnp.mean(axis=0), nnp.mean(axis=1), nnp.mean()],
                'variance': [nnp.var(axis=0), nnp.var(axis=1), nnp.var()],
                'standard deviation': [nnp.std(axis=0), nnp.std(axis=1), nnp.std()],
                'max': [nnp.max(axis=0), nnp.max(axis=1), nnp.max()],
                'min': [nnp.min(axis=0), nnp.min(axis=1), nnp.min()],
                'sum': [nnp.sum(axis=0), nnp.sum(axis=1), nnp.sum()]
                    }
        return calculations
    else:
        raise ValueError("List must contain nine numbers.")




