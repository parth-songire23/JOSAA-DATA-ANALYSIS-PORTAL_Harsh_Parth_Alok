# from django.shortcuts import render,HttpResponse
# from datetime import datetime
# from myapp.models import Contact
# import math
# from scipy.stats import norm
# import pandas as pd
# import matplotlib.pyplot as plt

# # Create your views here.
# def kun_index(request):
#     context={
#         "variable":"this is sent",
#     }
#     return render(request,"kun_index.html",context)
#     # return HttpResponse("this is home page of myapp")

# def about(request):
#     return render(request,"about.html")
# def services(request):
#     return render(request,"services.html")
# def predictor(request):
#     if request.method == "POST":
#         # Get the user inputs from the form
#         Seat_Type = request.POST.get("Seat_Type")
#         Rank = float(request.POST.get("Rank"))
#         College = request.POST.get("College")

#         # Load the cleaned data from the CSV file
#         df = pd.read_csv('ORCR_16_22_all.csv')
#         df = df[~(df['Opening_Rank'].str.endswith('P') | df['Closing_Rank'].str.endswith('P'))]

#         if College != "All":
#             df = df[~(df['Institute'] != College)]
        
#         df['Opening_Rank'] = df['Opening_Rank'].astype(float)

#         # Filter the data based on user inputs
#         filtered_data = df[(df['Seat_Type'] == Seat_Type) & (df['Opening_Rank'] >= Rank ) & (df['Round'] == 6)]

#         # Sort the filtered data by Opening Rank
#         filtered_data = filtered_data.sort_values('Opening_Rank')

#         # Convert the filtered data to a list of dictionaries
#         data_list = filtered_data.to_dict(orient='records')

#         # Pass the filtered data to the template
#         context = {
#             'Seat_Type': Seat_Type,
#             'Rank': Rank,
#             'filtered_data': data_list
#         }
#         return render(request, 'predictor.html', context)

#     return render(request, 'predictor.html')
# def contact(request):
#     ob={}
#     if request.method=="POST":
#         name=request.POST.get("name")
#         email=request.POST.get("email")
#         phoneNumber=request.POST.get("phoneNumber")
#         contact=Contact(name=name,email=email,phoneNumber=phoneNumber,date=datetime.today())
#         contact.save()
#         ob.update({"personname":name})
#     return render(request,"contact.html",ob)
# def info(request):
#     return render(request, "info.html")
# def questions(request):
#     return render(request, "questions.html")

# import io
# import base64

# def get_graph_as_base64():
#     # Create a buffer to hold the plot image
#     buffer = io.BytesIO()

#     # Save the plot to the buffer
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)

#     # Convert the plot image to base64 string
#     plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

#     # Close the buffer
#     buffer.close()

#     return plot_base64

# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure
# import io

# def trends(request):
#     # Load the data from the CSV file
#     df = pd.read_csv('ORCR_16_22_all.csv')

#     # Generate the line graph of opening rank trends over the years
#     fig = Figure()
#     ax = fig.add_subplot(111)
#     ax.plot(df['Year'], df['Opening_Rank'])
#     ax.set_xlabel('Year')
#     ax.set_ylabel('Opening Rank')
#     ax.set_title('Opening Rank Trends Over the Years')

#     # Convert the plot to a PNG image
#     canvas = FigureCanvas(fig)
#     buffer = io.BytesIO()
#     canvas.print_png(buffer)
#     buffer.seek(0)
#     graph = buffer.getvalue()

#     # Render the graph in the template
#     context = {'graph': graph}
#     return render(request, 'trends.html', context)


from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact
import math
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

def kun_index(request):
    context = {
        "variable": "this is sent",
    }
    return render(request, "kun_index.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def predictor(request):
    if request.method == "POST":
        # Get the user inputs from the form
        Seat_Type = request.POST.get("Seat_Type")
        Rank = float(request.POST.get("Rank"))
        College = request.POST.get("College")

        # Load the cleaned data from the CSV file
        df = pd.read_csv('ORCR_16_22_all.csv')
        df = df[~(df['Opening_Rank'].str.endswith('P') | df['Closing_Rank'].str.endswith('P'))]

        if College != "All":
            df = df[~(df['Institute'] != College)]
        
        df['Opening_Rank'] = df['Opening_Rank'].astype(float)

        # Filter the data based on user inputs
        filtered_data = df[(df['Seat_Type'] == Seat_Type) & (df['Opening_Rank'] >= Rank ) & (df['Round'] == 6)]

        # Sort the filtered data by Opening Rank
        filtered_data = filtered_data.sort_values('Opening_Rank')

        # Convert the filtered data to a list of dictionaries
        data_list = filtered_data.to_dict(orient='records')

        # Pass the filtered data to the template
        context = {
            'Seat_Type': Seat_Type,
            'Rank': Rank,
            'filtered_data': data_list
        }
        return render(request, 'predictor.html', context)

    return render(request, 'predictor.html')

def contact(request):
    ob = {}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phoneNumber = request.POST.get("phoneNumber")
        contact = Contact(name=name, email=email, phoneNumber=phoneNumber, date=datetime.today())
        contact.save()
        ob.update({"personname": name})
    return render(request, "contact.html", ob)

def info(request):
    return render(request, "info.html")

def questions(request):
    return render(request, "questions.html")

def get_graph_as_base64(fig):
    buffer = io.BytesIO()
    FigureCanvas(fig).print_png(buffer)
    buffer.seek(0)
    plot_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()
    return plot_base64

def trends(request):
    df = pd.read_csv('ORCR_16_22_all.csv')
    df = df[~(df['Opening_Rank'].str.endswith('P') | df['Closing_Rank'].str.endswith('P'))]

    filtered_data_1 = df[(df['Round'] == 6) & (df['Academic'] == 'Computer Science and Engineering (4 Years, Bachelor of Technology)') & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 2500) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]
    filtered_data_1['Closing_Rank'] = pd.to_numeric(filtered_data_1['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_1 = filtered_data_1.sort_values('Closing_Rank')
    if filtered_data_1.empty:
        error_message = 'No data available for the selected conditions.'
        context = {'error_message': error_message}
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_1['Closing_Rank'], filtered_data_1['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in CSE')
        graph1 = get_graph_as_base64(fig)
        context = {'graph1': graph1}

    filtered_data_2 = df[(df['Round'] == 6) & (df['Gender'] == 'Gender-Neutral') & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022) & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 8000)
                         & (df['Academic']=='Civil Engineering (4 Years, Bachelor of Technology)')]
    
    filtered_data_2['Closing_Rank'] = pd.to_numeric(filtered_data_2['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_2 = filtered_data_2.sort_values('Closing_Rank')

    if filtered_data_2.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_2['Closing_Rank'], filtered_data_2['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Institutes with closing rank less than 8000')
        graph2 = get_graph_as_base64(fig)
        context.update({'graph2': graph2})

    filtered_data_3 = df[(df['Round'] == 6) & (df['Gender'] == 'Gender-Neutral') & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022) & (pd.to_numeric(df['Closing_Rank'], errors='coerce') >= 8000)
                         & (df['Academic']=='Civil Engineering (4 Years, Bachelor of Technology)')]
    
    filtered_data_3['Closing_Rank'] = pd.to_numeric(filtered_data_3['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_3 = filtered_data_3.sort_values('Closing_Rank')

    if filtered_data_3.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_3['Closing_Rank'], filtered_data_3['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Institutes with closing rank greater than 8000')
        graph3 = get_graph_as_base64(fig)
        context.update({'graph3': graph3})

    filtered_data_4 = df[(df['Round'] == 6) & ((df['Academic'] == 'Mathematics and Computing (4 Years, Bachelor of Technology)') | (df['Academic'] == 'Mathematics and Computing (4 Years, Bachelor of Science)')) & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 7000) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]
    filtered_data_4['Closing_Rank'] = pd.to_numeric(filtered_data_4['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_4 = filtered_data_4.sort_values('Closing_Rank')

    if filtered_data_4.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_4['Closing_Rank'], filtered_data_4['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in MNC')
        graph4 = get_graph_as_base64(fig)
        context.update({'graph4': graph4})

    filtered_data_5 = df[(df['Round'] == 6) & (df['Academic'] == 'Electrical Engineering (4 Years, Bachelor of Technology)') & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 9000) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]

    filtered_data_5['Closing_Rank'] = pd.to_numeric(filtered_data_5['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_5 = filtered_data_5.sort_values('Closing_Rank')
    if filtered_data_5.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_5['Closing_Rank'], filtered_data_5['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in EE')
        graph5 = get_graph_as_base64(fig)
        context.update({'graph5': graph5})

    filtered_data_6 = df[(df['Round'] == 6) & (df['Academic'] == 'Mechanical Engineering (4 Years, Bachelor of Technology)') & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 9000) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]

    filtered_data_6['Closing_Rank'] = pd.to_numeric(filtered_data_6['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_6 = filtered_data_6.sort_values('Closing_Rank')
    if filtered_data_6.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_6['Closing_Rank'], filtered_data_6['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in Mech')
        graph6 = get_graph_as_base64(fig)
        context.update({'graph6': graph6})

    filtered_data_7 = df[(df['Round'] == 6) & (df['Academic'] == 'Chemical Engineering (4 Years, Bachelor of Technology)') & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 9000) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]

    filtered_data_7['Closing_Rank'] = pd.to_numeric(filtered_data_7['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_7 = filtered_data_7.sort_values('Closing_Rank')
    if filtered_data_7.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_7['Closing_Rank'], filtered_data_7['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in Chemical')
        graph7 = get_graph_as_base64(fig)
        context.update({'graph7': graph7})

    filtered_data_8 = df[(df['Round'] == 6) & (df['Academic'] == 'Civil Engineering (4 Years, Bachelor of Technology)') & (df['Gender'] == 'Gender-Neutral') & (pd.to_numeric(df['Closing_Rank'], errors='coerce') <= 9000) & (df['Seat_Type'] == 'OPEN') & (df['Year'] == 2022)]

    filtered_data_8['Closing_Rank'] = pd.to_numeric(filtered_data_8['Closing_Rank'], errors='coerce')  # Convert Closing Rank to numeric type
    filtered_data_8 = filtered_data_8.sort_values('Closing_Rank')
    if filtered_data_8.empty:
        error_message = 'No data available for the selected conditions.'
        context.update({'error_message': error_message})
    else:
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(filtered_data_8['Closing_Rank'], filtered_data_8['Institute'])
        ax.set_xlabel('Closing Rank')
        ax.set_ylabel('Institute')
        ax.set_title('Closing Rank Trends of IITs in Civil')
        graph8 = get_graph_as_base64(fig)
        context.update({'graph8': graph8})

    return render(request, 'trends.html', context)