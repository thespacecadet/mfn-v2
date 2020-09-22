

import numpy as np
import matplotlib.pyplot as plt
print('som started')

def closest_node(data, t, map, m_rows, m_cols):
  # (row,col) of map node closest to data[t]
  print('closest node')
  result = (0,0)
  small_dist = 1.0e20
  for i in range(m_rows):
    for j in range(m_cols):
      ed = euc_dist(map[i][j], data[t])
      if ed < small_dist:
        small_dist = ed
        result = (i, j)
  return result

def euc_dist(v1, v2):
  return np.linalg.norm(v1 - v2) 

def manhattan_dist(r1, c1, r2, c2):
  return np.abs(r1-r2) + np.abs(c1-c2)

def most_common(lst, n):
  # lst is a list of values 0 . . n
  if len(lst) == 0: return -1
  counts = np.zeros(shape=n, dtype=np.int)
  for i in range(len(lst)):
    counts[lst[i]] += 1
  return np.argmax(counts)

#replacement for most common algorithm.
#chooses one subject arbitrarily per point on the map
def most_common_replacement(lst):
  if len(lst) > 1:
    print ("more than one item in point!")
  if len(lst) >= 1:
    return lst[0]
  else:
    return -1

# ==================================================================

def som(tfidf_result,tfidf_labels,dimensions):
  # 0. get started
  np.random.seed(1)
  Dim = dimensions
  Rows = 20; Cols = 20
  RangeMax = Rows + Cols
  LearnMax = 0.5
  StepsMax = 3000

  # 1. load data
  #data_file = "./Data/iris_data_012.txt"
  
  data_x = np.array(tfidf_result)
  data_y = np.array(tfidf_labels)
  
  # 2. construct the SOM
  print("Constructing SOM, please wait...")
  map = np.random.random_sample(size=(Rows,Cols,Dim))
  for s in range(StepsMax):
    if s % (StepsMax/10) == 0: print("step = ", str(s))
    pct_left = 1.0 - ((s * 1.0) / StepsMax)
    curr_range = (int)(pct_left * RangeMax)
    curr_rate = pct_left * LearnMax

    t = np.random.randint(len(data_x))
    (bmu_row, bmu_col) = closest_node(data_x, t, map, Rows, Cols)
    for i in range(Rows):
      for j in range(Cols):
        if manhattan_dist(bmu_row, bmu_col, i, j) < curr_range:
          map[i][j] = map[i][j] + curr_rate * \
(data_x[t] - map[i][j])
  print("SOM construction complete \n")

  # associate each data point with a map node
  print("Associating each data label to one map node ")
  mapping = np.empty(shape=(Rows,Cols), dtype=object)
  for i in range(Rows):
    for j in range(Cols):
      mapping[i][j] = []

  for t in range(len(data_x)):
    (m_row, m_col) = closest_node(data_x, t, map, Rows, Cols)
    mapping[m_row][m_col].append(t)

  label_map = np.zeros(shape=(Rows,Cols), dtype=np.int)
  for i in range(Rows):
    for j in range(Cols):
      label_map[i][j] = most_common_replacement(mapping[i][j])
  som_data = [label_map,mapping]
  return som_data
