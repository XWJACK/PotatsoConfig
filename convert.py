import os

root_path = './Shadowrocket-ADBlock-Rules'
dist_path = './potatso'

try:
    os.makedirs(dist_path)
except:
    pass

os.system('git -C ./Shadowrocket-ADBlock-Rules reset --hard && git -C ./Shadowrocket-ADBlock-Rules pull')

def convert(name):
    fi_f = open(os.path.join(dist_path, name), 'w+')
    fi_f.write('ruleSets:\n')
    fi_f.write('- name: %s\n' % name)
    fi_f.write('  rules:\n')
    for line in open(os.path.join(root_path, fi)):
        if line.startswith('DOMAIN') or line.startswith('IP-CIDR'):
            fi_f.write('  - '+line)
    fi_f.write('  - GEOIP,CN,DIRECT\n')

for fi in os.listdir(root_path):
    fi_d = os.path.join(root_path, fi)
    if not os.path.isdir(fi_d) and fi.startswith('sr'):
        print(fi)
        convert(fi)
