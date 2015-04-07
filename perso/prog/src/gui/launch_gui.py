'''
Created on 30 juil. 2013

@author: gtheurillat
'''


import sys, time, locale, os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from perso.prog.src.gui.gui import Ui_GroupBox
from perso.prog.src.controller.cutimages import Cut_Images
from threading import Thread
from time import sleep

class MyStream(object):
    
    def __init__(self, logText):
        ""
        self.myLogText = logText
        
    
    def write(self, text):
        # Add text to a QTextEdit...
        self.myLogText.appendPlainText(text)
        QCoreApplication.processEvents
        self.myLogText.show()
    

class CutImages_GUI(QGroupBox):
    ""
    def __init__(self, parent=None):
        ""
        super (CutImages_GUI, self).__init__(parent)
        
        self.createWidget()
        self.param_data = {}
        self.msgBox = None
        self.thread_run = False
        
    def createWidget(self):
        ""
        self.ui = Ui_GroupBox()
        self.ui.setupUi(self)
        
        #set des slot pour les boutons
        self.ui.inputButton.clicked.connect(self._browse_inputfolder)
        self.ui.outputButton.clicked.connect(self._browse_outputfolder)
        self.ui.runButton.clicked.connect(self._start_generation)
        
        #mise en place du drop pour  les inputText
        self.ui.inputText.setAcceptDrops(True)
        self.ui.outputText.setAcceptDrops(True);
        self.ui.inputText.installEventFilter(self)
        self.ui.outputText.installEventFilter(self)
        
        #check manga lecture initialement
        self.ui.radioDG.setChecked(True)
        
        #rediection de la sortie standard vers un inputtext de log
        self.ui.logText.setReadOnly(True)
        self.ui.logText.clear()
        sys.stdout = MyStream(self.ui.logText)
        sys.stderr = MyStream(self.ui.logText) 
        
        self.proxy = Cut_Images()
        
    def thread_progressbar(self):
        ""
        value = 0
        while self.thread_run == True:
            if value >= 100:
                value = 0
            self._update_bar(value)
            value += 25
            sleep(0.25)
    
        

    def eventFilter(self, object, event):
        if (object is self.ui.inputText or object is self.ui.outputText):
            if (event.type() == QEvent.DragEnter):
                if event.mimeData().hasUrls():
                    event.accept()   # must accept the dragEnterEvent or else the dropEvent can't occur !!!
                    #print "accept"
                else:
                    event.ignore()
                    #print "ignore"
            if (event.type() == QEvent.Drop):
                if event.mimeData().hasUrls():   # if file or link is dropped
                    urlcount = len(event.mimeData().urls())  # count number of drops
                    url = event.mimeData().urls()[0]   # get first url
                    object.setText(url.path()[1:])   # assign first url to editline
                    #event.accept()  # doesnt appear to be needed
            return False # lets the event continue to the edit
        return False


    def _browse_outputfile(self):
        #fname = QFileDialog.getExistingDirectory(self, 'Select input file')
        filters = [self.tr('Epub (*.epub)'),]
        filename, filter_ =QFileDialog.getOpenFileNameAndFilter(None, "select output file", QDir.home().absolutePath(), ','.join(str(v) for v in filters))
        if filename:
            self.ui.inputText.setText(filename)
    
    def _browse_outputfolder(self):
        fname = QFileDialog.getExistingDirectory(self, 'Select output folder')
        if fname:
            self.ui.outputText.setText(fname)
    
    def _browse_inputfolder(self):
        fname = QFileDialog.getExistingDirectory(self, 'Select input folder')
        if fname:
            self.ui.inputText.setText(fname)
            
    def _start_generation(self):
        inputText = self.ui.inputText.text()
        outputext = self.ui.outputText.text()
        
#        self._show_loader()
        #self._show_ok()
        #self._show_ko()
        #self._show_echec()
        
        if inputText != "" and inputText != None:
            if outputext != "" and outputext != None:
                if os.path.isdir(inputText):
                    self._start_convertion(inputText, outputext)
                else:
                    self._show_warning("[WARNING] L'input doit etre un repertoire")
            else:
                self._show_warning("[WARNING] Absence de repertoire de sortie")
        else:
            self._show_warning("[WARNING] Absence de repertoire d'entree")
            
    
    
    def _start_convertion(self, input_folder, output_file):
        ""
        
        if os.path.exists(input_folder):
            try:
                isEuropeenLectureWay = True
                #recuperation du mode de lecture
                if self.ui.radioDG.isChecked() == True:
                    #sens de leture de gauche a droite (type manga)
                    isEuropeenLectureWay = False
                
                #on demarre le thread de la progressbar
                self._update_bar(0);
                thread = Thread(target = self.thread_progressbar, args = ())
                 
                self.thread_run = True
                thread.start()
                
                res, message = self.proxy.start(str(input_folder), str(output_file), isEuropeenLectureWay)
                if res == False:
                    self._show_ko(message)
                else:
                    self._show_ok()
                self.thread_run = False
                self._update_bar(100);
            except Exception, e:
                print e
                self._show_ko("[ERREUR] {0}".format(e))
        else:
            self._show_warning("[WARNING] Merci de verifier l'existance du repertoire d'entree.")
    
    def _update_bar(self, val):
        self.ui.progressBar.setValue(val)   
    
    
    def _show_loader(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setText("Exportation des notes en cours...");
        self.msgBox.setInformativeText("Merci de patienter");
        self.msgBox.setStandardButtons(QMessageBox.Cancel);
        
        icon = QPixmap("images/loader.jpg")
        self.msgBox.setIconPixmap(icon)
        self.msgBox.show()
         
    def _show_ko(self, message):
        self.msgBox = QMessageBox(self)
        self.msgBox.setText("Le decoupage des images a ECHOUE");
        self.msgBox.setInformativeText(message);
        self.msgBox.setStandardButtons(QMessageBox.Ok);
        
        icon = QPixmap("images/KO.png")
        self.msgBox.setIconPixmap(icon)
        self.msgBox.show()
        
    def _show_ok(self):
        self.msgBox = QMessageBox(self)
        self.msgBox.setText("Le decoupages des images a ete un succes");
        self.msgBox.setInformativeText("Merci et a bientot");
        self.msgBox.setStandardButtons(QMessageBox.Ok);
        
        icon = QPixmap("images/OK.png")
        self.msgBox.setIconPixmap(icon)
        self.msgBox.show()
        
    def _show_warning(self, message):
        self.msgBox = QMessageBox(self)
        self.msgBox.setText(message)
        self.msgBox.setStandardButtons(QMessageBox.Ok);
        
        icon = QPixmap("images/ECHEC.png")
        self.msgBox.setIconPixmap(icon)
        self.msgBox.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = CutImages_GUI()
    myapp.show()
    sys.exit(app.exec_())