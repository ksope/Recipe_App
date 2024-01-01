from io import BytesIO 
import base64
import matplotlib.pyplot as plt
from recipes.models import Recipe

def get_graph():
   #create a BytesIO buffer for the image
   buffer = BytesIO()         

   #create a plot with a bytesIO object as a file-like object. Set format to png
   plt.savefig(buffer, format='png')

   #set cursor to the beginning of the stream
   buffer.seek(0)

   #retrieve the content of the file
   image_png=buffer.getvalue()

   #encode the bytes-like object
   graph=base64.b64encode(image_png)

   #decode to get the string as output
   graph=graph.decode('utf-8')

   #free up the memory of buffer
   buffer.close()

   #return the image/graph
   return graph

#chart_type: user input o type of chart,
#data: pandas dataframe
def get_chart(chart_type, data,  **kwargs):
   #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
   #AGG is preferred solution to write PNG files
    plt.switch_backend('AGG')

   #specify figure size
    fig=plt.figure(figsize=(5,5))

    #select chart_type based on user input from the form
    if chart_type == '#1':

        color = ['orange', 'blue', 'red', 'yellow', 'green'] 
       #plot bar chart between recipes on x-axis and cooking time on y-axis
        plt.xlabel('Recipes')
        plt.ylabel('Cooking Time (mins)')
        plt.bar(data['name'], data['cooking_time'], color=color)
        plt.legend()
        plt.title('Recipe Cooking Times')
       

    elif chart_type == '#2':
        #generate pie chart based on the price.
        #The cooking times are sent from the view as labels
        plt.pie(data['cooking_time'], labels=data['name'].values)
        plt.legend(loc='upper left')
        plt.title('Recipe Cooking Times')

    elif chart_type == '#3':
        #plot bar chart between recipes on x-axis and cooking time on y-axis
        plt.xlabel('Recipes')
        plt.ylabel('Cooking Time (mins)')
        plt.plot(data['name'], data['cooking_time'])
        plt.legend()
        plt.title('Recipe Cooking Times')

    else:
        print ('unknown chart type')

    #specify layout details
    plt.tight_layout()

    #render the graph to file
    chart =get_graph() 
    return chart 

