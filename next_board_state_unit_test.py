from game_of_life import next_board_state
#******************** REWORK DUE TO BOARD WRAPPING REQUIREMENT ********************

if __name__ == "__main__":
  #TEST 1: live cells with 0(a) or 1(b) live neighbors becomes dead

  init_state1a1 = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
  ]
  init_state1a2 = [
    [0,0,0],
    [0,0,0],
    [0,0,1]
  ]
  init_state1b1 = [
    [1,0,0],
    [0,1,0],
    [0,0,0]
  ]
  init_state1b2 = [
    [0,0,0],
    [0,1,1],
    [0,0,0]
  ]
  expected_next_state1 = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
  ]
  init_state1c1 = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,1,1,1,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
  ]
  expected_next_state1c1 = [
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0]
  ]
  actual_next_state1a1 = next_board_state(init_state1a1)
  actual_next_state1a2 = next_board_state(init_state1a2)
  actual_next_state1b1 = next_board_state(init_state1b1)
  actual_next_state1b2 = next_board_state(init_state1b2)
  actual_next_state1c1 = next_board_state(init_state1c1)

  if actual_next_state1a1 == expected_next_state1:
    print('PASSED 1a1')
  else:
    print('FAILED 1a1')
    print('Expected:')
    print(expected_next_state1)
    print('Actual:')
    print(actual_next_state1a1)
  if actual_next_state1a2 == expected_next_state1:
    print('PASSED 1a2')
  else:
    print('FAILED 1a2')
    print('Expected:')
    print(expected_next_state1)
    print('Actual:')
    print(actual_next_state1a2)
  if actual_next_state1b1 == expected_next_state1:
    print('PASSED 1b1')
  else:
    print('FAILED 1b1')
    print('Expected:')
    print(expected_next_state1)
    print('Actual:')
    print(actual_next_state1b1)
  if actual_next_state1b2 == expected_next_state1:
    print('PASSED 1b2')
  else:
    print('FAILED 1b2')
    print('Expected:')
    print(expected_next_state1)
    print('Actual:')
    print(actual_next_state1b2)
  if actual_next_state1c1 == expected_next_state1c1:
    print('PASSED 1c1')
  else:
    print('FAILED 1c1')
    print('Expected:')
    print(expected_next_state1c1)
    print('Actual:')
    print(actual_next_state1c1)
  #TEST 2 Edge/corner wrap detection
  #Incorprate edge detection for each edge and corner.  Try to combine edges and corners in test? (research)
  #null board
  init_state_null = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
  ]
  expected_next_state_null = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
  ]
  #central with no edge wrapping
  init_state2a1 = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
  ]
  expected_next_state2a1 = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
  ]
  init_state2a2 = [
    [0,0,0,0,0],
    [0,0,1,1,0],
    [0,0,1,1,0],
    [0,0,0,1,0],
    [0,0,0,0,0]
  ]
  expected_next_state2a2 = [
    [0,0,0,0,0],
    [0,0,1,1,0],
    [0,0,0,0,1],
    [0,0,1,1,0],
    [0,0,0,0,0]
  ]
  #edge testing
  init_state2b1 = [
    [0,0,1,1,0],
    [0,0,1,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0],
    [0,0,0,1,0]
  ]
  expected_next_state2b1 = [
    [0,0,0,0,1],
    [0,0,0,0,1],
    [0,0,0,1,1],
    [0,0,1,1,1],
    [0,0,0,1,1]
  ]
  init_state2b2 = [
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1]
  ]
  expected_next_state2b2 = [
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [0,1,0,1,0]
  ]
  init_state2c1 = [
    [1,1,1,1,1],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [1,1,1,1,1]
  ]
  expected_next_state2c1 = [
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,0,0],
    [1,1,1,1,1],
    [0,0,0,0,0]
  ]
  init_state2c2 = [
    [1,1,1,1,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,0,0,0,1],
    [1,1,1,1,1]
  ]
  expected_next_state2c2 = [
    [0,0,0,0,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,0,0,0,0]
  ]
  init_state2c3 = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1]
  ]
  expected_next_state2c3 = [
    [0,1,0,1,0],
    [1,1,1,1,1],
    [0,1,0,1,0],
    [1,1,1,1,1],
    [0,1,0,1,0]
  ]
  init_state2c4 = [
    [0,1,1,1,0],
    [1,0,1,0,1],
    [1,1,0,1,1],
    [1,0,1,0,1],
    [0,1,1,1,0]
  ]
  expected_next_state2c4 = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0]
  ]
  actual_next_state_null = next_board_state(init_state_null)
  actual_next_state2a1 = next_board_state(init_state2a1)
  actual_next_state2a2 = next_board_state(init_state2a2)
  actual_next_state2b1 = next_board_state(init_state2b1)
  actual_next_state2b2 = next_board_state(init_state2b2)
  actual_next_state2c1 = next_board_state(init_state2c1)
  actual_next_state2c2 = next_board_state(init_state2c2)
  actual_next_state2c3 = next_board_state(init_state2c3)
  actual_next_state2c4 = next_board_state(init_state2c4)

  if expected_next_state_null == actual_next_state_null:
    print('PASSED NULL STATE')
  else:
    print('FAILED NULL STATE!')
    print('Expected:')
    print(expected_next_state_null)
    print('Actual:')
    print(actual_next_state_null)
  if expected_next_state2a1 == actual_next_state2a1:
    print('PASSED 2a1!')
  else:
    print('FAILED 2a1!')
    print('Expected:')
    print(expected_next_state2a1)
    print('Actual:')
    print(actual_next_state2a1)
  if expected_next_state2a2 == actual_next_state2a2:
    print('PASSED 2a2!')
  else:
    print('FAILED 2a2!')
    print('Expected:')
    print(expected_next_state2a2)
    print('Actual:')
    print(actual_next_state2a2)
  if expected_next_state2b1 == actual_next_state2b1:
    print('PASSED 2b1!')
  else:
    print('FAILED 2b1!')
    print('Expected:')
    print(expected_next_state2b1)
    print('Actual:')
    print(actual_next_state2b1)
  if expected_next_state2b2 == actual_next_state2b2:
    print('PASSED 2b2!')
  else:
    print('FAILED 2b2!')
    print('Expected:')
    print(expected_next_state2b2)
    print('Actual:')
    print(actual_next_state2b2)
  if expected_next_state2c1 == actual_next_state2c1:
    print('PASSED 2c1!')
  else:
    print('FAILED 2c1!')
    print('Expected:')
    print(expected_next_state2c1)
    print('Actual:')
    print(actual_next_state2c1)
  if expected_next_state2c2 == actual_next_state2c2:
    print('PASSED 2c2!')
  else:
    print('FAILED 2c2!')
    print('Expected:')
    print(expected_next_state2c2)
    print('Actual:')
    print(actual_next_state2c2)
  if expected_next_state2c3 == actual_next_state2c3:
    print('PASSED 2c3!')
  else:
    print('FAILED 2c3!')
    print('Expected:')
    print(expected_next_state2c3)
    print('Actual:')
    print(actual_next_state2c3)
  if expected_next_state2c4 == actual_next_state2c4:
    print('PASSED 2c4!')
  else:
    print('FAILED 2c4!')
    print('Expected:')
    print(expected_next_state2c4)
    print('Actual:')
    print(actual_next_state2c4)