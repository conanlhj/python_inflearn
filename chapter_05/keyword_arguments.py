def print_something(m_name,y_name):
    print('mine : {}, yours : {}'.format(m_name,y_name))

print_something('HJ','DM')
print_something(y_name = 'DM', m_name = 'HJ')

def print_something(m_name,y_name='BS'):
    print('mine : {}, yours : {}'.format(m_name,y_name))

print_something('HJ')
print_something(y_name = 'DM', m_name = 'HJ')
