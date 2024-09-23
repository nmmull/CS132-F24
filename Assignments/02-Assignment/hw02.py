from sympy import *

def leading_entry_index(a):
  for i in range(len(a)):
    if a[i] != 0:
      return i
  return None

def is_echelon(a):
  curr_row = 0
  prev_lead = -1
  while curr_row < a.rows:
    next_lead = leading_entry_index(a.row(curr_row))
    if next_lead is not None:
      if prev_lead < next_lead:
        curr_row += 1
        prev_lead = next_lead
      else:
        return False
    else:
      return leading_entry_index(a[curr_row:,:]) is None
  return True

def is_rref(a):
  curr_row = 0
  prev_lead = -1
  while curr_row < a.rows:
    next_lead = leading_entry_index(a.row(curr_row))
    if next_lead is not None:
      if prev_lead < next_lead \
         and a[curr_row, next_lead] == 1 \
         and a[:curr_row, next_lead].is_zero_matrix:
        curr_row += 1
        prev_lead = next_lead
      else:
        return False
    else:
      return leading_entry_index(a[curr_row:,:]) is None
  return True

def back_sub(a):
  for curr_row in range(a.rows):
    curr_lead_ind = leading_entry_index(a[curr_row,:])
    if curr_lead_ind is not None:
      curr_lead = a[curr_row, curr_lead_ind]
      a[curr_row,:] /= curr_lead
      for i in range(curr_row):
        a[i,:] += (-1) * a[i, curr_lead_ind] * a.row(curr_row)
    else:
      return
