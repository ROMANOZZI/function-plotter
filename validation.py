
from tkinter import messagebox
#case 1





def validate_in(s,min,max):
  message=""
  if (not s or not min or not max):
     message="please fill the required fields"
  else:


     if(min.isnumeric()==False):
         message="minimum value of the range must be numerical value"
     elif(max.isnumeric()==False):
         message = "maximum value of the range must be numerical value"
     if(min>max):
         message="range inputs is invalid"
     count=0
     for i in s:
       count=count+1
     if(i.isalpha()and i.lower()!="x"):

       if(count>1):
          message="the input is not valid mathematical equation"
       elif(count==1):
          message="the input is not function of x"
     for i in s:
       if(i=="x"):

         try:
             if(s[s.index(i)+1].isnumeric()or s[s.index(i)+1].isalpha()):
                  message = "invalid operator after x"
         except:
             message="invalid operator after x"

             if(s[s.index(i)-1].isnumeric()or s[s.index(i)-1].isalpha()):
                  print(s[s.index(i) - 1].isnumeric() , s[s.index(i) - 1].isalpha())
                  message="invalid operator before x"

  messagebox.showerror(title="Error",message=message)
  return None