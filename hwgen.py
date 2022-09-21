import os
import sys
from configparser import ConfigParser

class ReadConfig:
    def __init__(self, filepath=None):
        if filepath:
            configPath = filepath
        else:
            curPath = os.path.dirname(os.path.realpath(sys.argv[0]))
            configPath = os.path.join(curPath, "config.ini")
        self.cf = ConfigParser()
        self.cf.read(configPath, encoding="utf-8-sig")

    def datapath(self, param):
        value = self.cf.get("datapath", param)
        return value

    def mask(self, param):
        value = self.cf.get("mask", param)
        return value

    def question(self, param):
        value = self.cf.get("question", param)
        return value

    def excel(self, param):
        value = self.cf.get("excel", param)
        return value
        
class HwGen:
    def __init__(self, class_id, configFile):
        self.buffer = []
        self.question_path = configFile.datapath('question_path')
        self.hw_ind = configFile.question('homework_ind')
        self.question_ind = configFile.question('question_ind')
        self.post_path = configFile.datapath("source_path") + '/' + class_id + '/' + self.hw_ind + '/' + self.hw_ind
    def gen_info_region(self):
        self.buffer.append('#*****请用utf-8方式打开及保存本文件****#\n')
        self.buffer.append('#*****请只修改相关区域，不要修改其余***#\n')
        self.buffer.append('#**********Homework %s****************#\n' % self.hw_ind)
        self.buffer.append('#*****Below is peronal info region*****#\n')
        self.buffer.append('#ID:                  \n')
        self.buffer.append('#name:                \n')
        self.buffer.append('#email:               \n')
    def gen_import_region(self):
        self.buffer.append('#*****Below is Import region***********#\n')
        self.buffer.append('#*****You can add line if needed*******#\n')
        self.buffer.append('\n')
        self.buffer.append('\n\n')
    def gen_assign_region(self):
        q_str = self.question_ind
        q_list = q_str.split(',')
        q_files = [q+'.py' for q in q_list]
        for q in q_files:
            in_anno = False
            q_name = self.question_path + '/' + q
            with open (q_name, 'r') as f:
                q_lines = f.readlines()
            for q_l in q_lines:
                if in_anno == True:
                    if q_l == "    '''\n":
                        in_anno = False
                    continue
                elif q_l == "    '''\n":
                    in_anno = True
                    continue
                else:
                    self.buffer.append(q_l)
            self.buffer.append('\n\n\n\n\n')
            #self.buffer.append('    #*****Code region end for this function*****#\n')
    def gen_write(self):
        hw_post = self.post_path + '.py'
        with open(hw_post,'w') as f:
           for l in self.buffer:
               f.write(l)
               
    def gen_liner(self):
        self.gen_info_region()
        self.gen_import_region()
        self.gen_assign_region()
        self.gen_write()
        
    
if __name__=='__main__':
    conf = ReadConfig()
    class_list = conf.datapath('class_path')
    class_list = class_list.split(',')
    for cls in class_list:
        hwgenTA = HwGen(cls, conf)
        hwgenTA.gen_liner()
