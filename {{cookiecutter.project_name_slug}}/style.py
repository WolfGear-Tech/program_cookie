def style(): return  """
            
QWidget {
    font-family: "Comic Sans MS";
    font-size: 18px;
    background-color: #f0f0f0;
}

QPushButton, QLineEdit { 
    border-style: outset;
    border-radius: 5px;
    border-width: 1px;
    border-color: rgb(134, 134, 134);
}

QPushButton:hover { 
    background-color: rgb(212, 212, 212); 
    border-color: rgb(100, 100, 100);
}

QPushButton:disabled { 
    background-color: rgb(182, 182, 182); 
}

"""