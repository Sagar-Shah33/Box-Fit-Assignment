from flask import Flask , jsonify , request , render_template
import pandas as pd

app = Flask(__name__)

class ConcepServe_Exception():
    def error(self):
        return "Item Greater than 15!"

class ConceptServe_Box(ConcepServe_Exception):
    def __init__(self):
        pass
        self.maxweight = []
        self.values = []
        self.r = dict() 
        self.ex = [] 
        self.ans = []     
    def read_file(self,filename):
        ccfile = open(filename)
        for aline in ccfile:
           values = aline.split(":")
           self.maxweight.append(int(values[0]))
           self.values.append(values[1]) 
        
        for i in range(len(self.values)):
            self.box(self.values[i],self.maxweight[i])  
            
    def box(self,data,boxweight):
        # print(data)
        data = pd.DataFrame(eval(data),columns=['index','weight','cost'])
        # print(data)
        # print(boxweight)
        # print(data)
        self.current = 0
        self.i = 0
        Lst = []
        cw = []
                
        for index,row in data.iterrows():
            cw.append(row['cost']/row['weight']+row['cost'])
        
        data['cost/weight'] = cw
        
        data = data.sort_values(by=["cost/weight"],ascending=False)
        
        global result
        result = data
        for index,row in data.iterrows():
            if((row['weight']+self.current) <= boxweight):
                self.current = row['weight'] + self.current
                self.somecost = row['cost']
                self.i+=1
                Lst.append(int(row['index']))

        if self.i <= 15:
            if(len(Lst)>0):
                listToStr = ','.join([str(elem) for elem in Lst])
                # print(listToStr)
                self.ans.append(listToStr)
            else:
                # print("-")
                self.ans.append("-")
        else:
            print(self.error())
    
 
# obj = ConceptServe_Box()
# obj.read_file("sample_input.txt") 
    


@app.route('/',methods=['GET','POST'])
def filename():
    if request.method == "POST":
        filename = request.form.get('sample')
        print(filename)
        obj = ConceptServe_Box()
        obj.read_file(filename)
        return render_template('index.html',result=obj.ans)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
