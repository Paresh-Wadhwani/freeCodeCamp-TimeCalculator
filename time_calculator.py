def add_time(start, duration, weekDay1 = ''):

  weekDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

  s_indexOfColon = start.find(':')
  s_indexOfSpace = start.find(' ')
  s_hours = start[:s_indexOfColon]
  s_mins = start[s_indexOfColon + 1:s_indexOfSpace]
  s_ap = start[s_indexOfSpace + 1:]

  s_ap_ = 'AM' if s_ap == 'PM' else 'PM'

  d_indexOfColon = duration.find(':')
  d_hours = duration[:d_indexOfColon]
  d_mins = duration[d_indexOfColon + 1:]

  f_mins = str(int(s_mins) + int(d_mins))

  f_hours = str(int(s_hours) + int(d_hours) + int(int(f_mins)/60))
  f_mins = str(int(f_mins) % 60)
  temp = int(int(f_hours) / 12)
  f_ap = s_ap if temp % 2 == 0 else s_ap_
  f_hours = str((int(f_hours) % 12))
  f_hours = '12' if f_hours == '0' else f_hours
  f_mins = '0' + f_mins
  f_mins = f_mins[-2:]

  f_days_ = int(int(d_hours) / 24)

  if s_ap == 'PM' and f_ap == 'AM':
    f_days_ += 1
  
  f_wDay = ''

  if weekDay1 != '':
    s_index = weekDays.index(weekDay1.capitalize())
    s_index += f_days_
    s_index %= 7
    f_wDay = ', ' + weekDays[s_index]

  f_days = '' if f_days_ == 0 else (' (next day)' if f_days_ == 1 else ' (' + str(f_days_) + ' days later)')

  new_time = f_hours + ':' + f_mins + ' ' + f_ap + f_wDay + f_days

  return new_time