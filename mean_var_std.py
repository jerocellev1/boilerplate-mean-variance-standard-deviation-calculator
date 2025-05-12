import numpy as np
def calculate():

  first_list = [9,  1,  7,  8,  4,  6,  9, 10, 5]
  np_list = np.array(first_list).reshape(3,3) # Convert list to a 3x3 numPy array named np_list
  my_dict = {   
    'mean': [np.mean(np_list, axis=0).tolist(), np.mean(np_list, axis=1).tolist(), np.mean(np_list.flatten()).tolist()],
    'variance': [np.var(np_list, axis=0).tolist(), np.var(np_list, axis=1).tolist(), np.var(np_list.flatten()).tolist()],
    'standard': [np.std(np_list, axis=0).tolist(), np.std(np_list, axis=1).tolist(), np.std(np_list.flatten()).tolist()],
    'max': [np.max(np_list, axis=0).tolist(), np.max(np_list, axis=1).tolist(), np.max(np_list.flatten()).tolist()],
    'min': [np.min(np_list, axis=0).tolist(), np.min(np_list, axis=1).tolist(), np.min(np_list.flatten()).tolist()],
    'sum': [np.sum(np_list, axis=0).tolist(), np.sum(np_list, axis=1).tolist(), np.sum(np_list.flatten()).tolist()]
    }
  size = len(first_list) # Use the numpy array for size calculation

  if size != 9:
    raise ValueError('List must contain nine numbers')
  else:
    return my_dict

calculate()
