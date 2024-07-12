def solution(m, n, startX, startY, balls):
  answer = []

  def simulation(ball):
    ballX, ballY = ball
    distances = []
    # 위쪽벽에 부딪힐 경우
    if not (startX == ballX and startY < ballY):
      distances.append((ballX - startX)**2 + (n - startY + n - ballY)**2)
    # 아래벽에 부딪힐 경우
    if not (startX == ballX and startY > ballY):
      distances.append((ballX - startX)**2 + (startY + ballY)**2)
    # 왼쪽벽에 부딪힐 경우
    if not (startX > ballX and startY == ballY):
      distances.append((startX + ballX)**2 + (startY - ballY)**2)
    # 오른쪽벽에 부딪힐 경우
    if not (startX < ballX and startY == ballY):
      distances.append((m - startX + m - ballX)**2 + (startY - ballY)**2)

    return min(distances)

  for ball in balls:
    answer.append(simulation(ball))
  return answer
