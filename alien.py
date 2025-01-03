alien_0={'name' : 'alex','color':'pink','x_position':0,'y_position':25,'speed':'medium'}
print(alien_0['color'])
print(alien_0['name'])
alien_0['x_position']=0
alien_0['y_position']=25
print(f"Original position:{alien_0['x_position']}")

#向右移动过=外星人
#根据当前速度确定外星人向右移动多远
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else :
    #这外星人移动快
    x_increment=3

alien_0['x_position']=alien_0['x_position']+x_increment
print(f"new position:{alien_0['x_position']}")