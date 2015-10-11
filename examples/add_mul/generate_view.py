import shutil, os
templatefile = os.path.join('templates', 'template.html')
viewfile = os.path.join('templates', 'view.html')
with open(templatefile, 'r') as f:
    lines = f.readlines()
with open(viewfile, 'w') as f:
    for line in lines:
        if line.startswith('INCLUDE:'):
            filename = line.split(':')[1].strip() + '.html'
            if os.path.isfile(filename):
                with open(filename, 'r') as f2:
                    text = f2.read()
                f.write(text + '\n')
        else:
            f.write(line + '\n')
