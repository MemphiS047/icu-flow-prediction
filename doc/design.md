# Foreword
The design is conformed of several explanations on the things that are aim to be done in the project the whole project is shaped with this document. Planning is done using Trello/Jira. For more information on things that have been done and things that will be done check out the following Trello/Jira [link](https://trello.com/b/x9LWes30/project-management-current-mybs)

# Added Value
1.  We can extract additional features from the regulations of UK, US and TR.
2.  If there is such data on the MIMIC-III, using those we can generate target features 
    and then train with the resulted dataset
3.  Comparison between models could be improved. For example, using 4 model or higher 
    we can draw a clear distinction between the models with the score values
4.  We can draw a conclusion from benefits of turning the problem into classification, 
    also need a review on that
5.  Distinction could be made between PICU, NICU and other ICU types as well and 
    benefits of it could be explained in the paper


<blockquote>
  <h3>🚧 Warning</h3>
  <p>It is important to note that the information related to poisoning in MIMIC-III may not be comprehensive or completely accurate, as it is dependent on how the data was collected and recorded in the electronic health record. Therefore, careful consideration should be given to how this information is used in research studies, and any limitations or potential biases in the data should be taken into account.</p>
</blockquote>

# ICU Flow
For building accuracte predictive modal for ICU flow we need to first define the whole ICU process/flow in order to extract relevant features and built relevant modals. The phases are defined by scannig through related research done from an extensive litreature review/analysis. 

# Roadmap
Roadmap is divided into 4 parts, each part have an end goal and things to do which all of them are listed in the Trello Kanban board.

## Part 1
For the first part the whole ICU flow prediction modal should be done, for part 1 in the kanban board the tasks are tagged with the relevant part and phase of each part (meaning the model that is being developed for that specific ICU flow)

## Part 2
Part 2 is only focused on writing the research paper that is about the whole process of building the ICU flow prediction modal

## Part 3
Part 3 is about deployment of the modal, building the mybs-heartbeat and mybs-web-app. 

## Part 4
This part is only focused on writing the research paper about the built system (icu-flow-prediction-modal / mybs-heartbeat / mybs-web-app). 