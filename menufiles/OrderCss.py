order_style = """

    QGroupBox, QWidget#TabOra, QWidget, QLabel#Image{
        background-color:orange;
    }

    QLabel#Image{
        padding: 12px;
    }

    QGroupBox{
        font-size: 20px;
        font-weight:bold;
        margin: 5px;
        color:darkred;
        padding: 20px 15px 10px 15px;
    }

    QGroupBox, QTabWidget, QLabel#Title, QPushButton, QLabel#InTitle{
        font-family:"Tahoma";
    }

    QWidget#TabRed{
        background-color:red;
    }

    QWidget#Side, QRadioButton{
        background-color:white;
    }

    QWidget#Boarder{
        border: 4px solid red;
    } 

    QRadioButton{
        border: 1px dashed black;
    }

    QLabel, QRadioButton{
        font-family:"Arial";
        font-size:15px;
    }

     QLabel#Title, QPushButton, QTabWidget{
        font-size: 16px;
    }

    QLabel#Title, QPushButton{
        padding:10px 5px;
        border-radius: 5px;
        font-weight:bold;      
    }

    QLabel#InTitle, QLabel#SmTitle, QRadioButton#RadTitle{
        color: darkred;
        font-weight: bold;
    }
    
    QLabel#InTitle{
        font-size: 18px;
    }

    QRadioButton#RadTitle{
        background-color:none;
        border: none;
    }

    QLabel#SmTitle{
        font-size: 16px;
    }   

    QWidget#Boarder, QLabel#Image, QWidget#Side, QWidget#TabOra, QWidget#TabRed, QLabel#Title, QPushButton, QGroupBox {
        border-radius: 10px;
    }

    QLabel#Title{
        border: 2px solid white;
    }
    
    QPushButton:hover{
        color: white;   
    }
    
    QPushButton:pressed{
        background-color: rgb(155, 105, 0);   
    }
    
"""