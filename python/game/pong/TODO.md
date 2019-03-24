## pong.py - to do list

  - Better color/font for score text.
  - Sound
      - Example: ``tone.play('A3', 1)`` - when bats are hit.
  - Game improvements - reducing size bat over time.
      - May need to define 'bats' as something other than Actor then.
  - Improve collision-based ball/bat test.
      - Keep last_ball_pos as well as ball. Collision test is then: line-collsion between (last_ball_pos -> ball_pos) and (bat_top -> bat_bottom).
  - ...
