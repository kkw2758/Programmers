# 동영상 처음 위치 : 0 분 0초
# prev : 10초 전으로 이동
# next : 10초 후로 이동
# 오프닝 건너뛰기 : 현재 재생 위치가 오프닝 구간(op_start <= 현재 재생 위치 <= op_end)인 경우 자동으로 오프닝 끝나는 위치로 이동


# EX) video_len, pos, op_start, op_end, commands
def change_minute(time):
  result = 0
  hour, minute = map(int, time.split(":"))
  result += (hour * 60 + minute)
  return result


def change_time_format(minute):
  hour = str(minute // 60).zfill(2)
  minute = str(minute % 60).zfill(2)
  return ":".join([hour, minute])


def solution(video_len, pos, op_start, op_end, commands):
  video_len = change_minute(video_len)
  pos = change_minute(pos)
  op_start = change_minute(op_start)
  op_end = change_minute(op_end)

  if op_start <= pos <= op_end:
    pos = op_end

  for command in commands:
    if command == "next":
      pos += 10
    elif command == "prev":
      pos -= 10
    if pos < 0:
      pos = 0
    if pos > video_len:
      pos = video_len
    if op_start <= pos <= op_end:
      pos = op_end

  return change_time_format(pos)
