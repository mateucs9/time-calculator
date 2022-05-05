def add_time(start, duration, *args):
  am_pm = start[-2:]
  hours = int(start.split(':')[0]) if am_pm == 'AM' else int(start.split(':')[0]) + 12
  minutes = int(start.split(':')[1].split()[0])

  day_dict = {0: 'monday', 1: 'tuesday', 2: 'wednesday', 3: 'thursday', 4: 'friday', 5: 'saturday', 6: 'sunday'}

  add_hours = int(duration.split(':')[0])
  add_minutes = int(duration.split(':')[1])
  
  new_hours = (hours + add_hours + (minutes + add_minutes) // 60) % 24
  new_minutes = (minutes + add_minutes) % 60
  new_days = (hours + add_hours + (minutes + add_minutes) // 60) // 24

  new_time = ''

  if new_hours > 12:
    print(new_hours)  
    new_time += "{}:{:02d} PM".format(new_hours-12, new_minutes)
  elif new_hours == 12 and new_minutes > 0:
    new_time += "{}:{:02d} PM".format(new_hours, new_minutes)
  elif new_hours == 0:
    new_time += "{}:{:02d} AM".format(new_hours+12, new_minutes)
  else:
    new_time += "{}:{:02d} AM".format(new_hours, new_minutes)

  if args:
    day_num = list(day_dict.keys())[list(day_dict.values()).index(args[0].lower())]
    new_day_week = day_dict[(day_num + new_days) % 7]
    new_time += ', {}'.format(new_day_week.title())
  
  if new_days >= 2:
    new_time += ' ({} days later)'.format(new_days)
  elif new_days == 1:
    new_time += ' (next day)'


  return new_time