AUTHORS:
Dylan Dizon
Keenan Hanearin-Balczer
Zachary McSweeny

TO RUN:
Ensure that and_tree_node.py, hard_constraints.py, main.py, prob_set.py, search_process.py, and soft_constraints.py are in the same folder
Place input file in the same folder as main.py, navigate to the folder in the terminal, and run the following:

```
python main.py [filename] [w_min_filled] [w_pref] [w_pair] [w_sec_diff] [pen_game_min] [pen_practice_min] [pen_not_paired] [pen_section]
```

Replace all bracketed text with the corresponding info. For example, [filename] = minnumber.txt
Note that the brackets are purely for clarity in this document, and should not be included in the terminal command

RESULTS:

There was not enough time for us to run and wait for the whole search to finish to find the best optimal schedule, so this is the best we could get. (apologies)

CPSC433F24-LargeInput1.txt ->
Eval:  7935
Node at Depth 48:
  Parent Node Depth: 47
  Slot(Day=MO, StartTime=8:00, MaxGames=2, MinGames=1, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U19T1 DIV 01', 'CUSA O35T1 DIV 02'], AssignedPractices=[])
  Slot(Day=MO, StartTime=9:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CSSC O19T1 DIV 01', 'CSSC O19T1 DIV 02', 'CSSC O19T1 DIV 03', 'CSSC O19T1 DIV 04', 'CMSA U07T1 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=10:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U08T1 DIV 01', 'CMSA U09T1 DIV 01', 'CMSA U09T1 DIV 02', 'CMSA U10T1 DIV 01', 'CMSA U10T1 DIV 02'], AssignedPractices=[])
  Slot(Day=MO, StartTime=11:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U12T1 DIV 01', 'CMSA U12T5 DIV 01', 'CMSA U15T1 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=12:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U10T2 DIV 01', 'CMSA U13T1 DIV 01', 'CMSA U15T2 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=13:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U11T1 DIV 01', 'CMSA U13T2 DIV 01', 'CMSA U15T3 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=14:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U11T2 DIV 01', 'CMSA U13T3 DIV 01', 'CMSA U15T4 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=15:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U12T2 DIV 01', 'CMSA U13T4 DIV 01', 'CMSA U13T4 DIV 02', 'CMSA U15T5 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=16:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U12T3 DIV 01', 'CMSA U13T5 DIV 01', 'CMSA U16T1 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=17:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U12T4 DIV 01', 'CMSA U14T1 DIV 01', 'CMSA U16T2 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=18:00, MaxGames=1, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CSSC O19T1 DIV 95'], AssignedPractices=[])
  Slot(Day=MO, StartTime=19:00, MaxGames=1, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U14T2 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=20:00, MaxGames=1, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U14T2 DIV 02'], AssignedPractices=[])
  Slot(Day=TU, StartTime=8:00, MaxGames=2, MinGames=1, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U19T2 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=9:30, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U14T3 DIV 01', 'CMSA U16T3 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=11:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=12:30, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U14T4 DIV 01', 'CMSA U16T4 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=14:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U17T2 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=15:30, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CUSA O35T1 DIV 01', 'CMSA U19T3 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=17:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U17T3 DIV 01', 'CUSA O19T1 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=18:30, MaxGames=1, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U17T4 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=8:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=1, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=9:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=10:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=11:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=12:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=13:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=14:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=15:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=16:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=17:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=18:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=19:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=20:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=8:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=1, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=9:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=10:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=11:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=12:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=13:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=14:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=15:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=16:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=17:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=18:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=['CMSA U12T1S', 'CMSA U13T1S'])
  Slot(Day=TU, StartTime=19:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=20:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=8:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=10:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=12:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=14:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=16:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=18:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Remaining Games: {'CMSA U19T4 DIV 01'}
  Remaining Practices: {'CMSA U08T1 DIV 01 PRC 01', 'CSSC O19T1 DIV 02 PRC 12', 'CMSA U16T1 PRC 01', 'CMSA U13T5 PRC 01', 'CMSA U15T5 PRC 01', 'CMSA U17T2 PRC 01', 'CSSC O19T1 DIV 03 PRC 18', 'CMSA U09T1 PRC 07', 'CUSA O35T1 PRC 01', 'CMSA U14T2 DIV 02 PRC 04', 'CMSA U14T3 PRC 02', 'CMSA U14T3 PRC 03', 'CSSC O19T1 DIV 02 PRC 08', 'CSSC O19T1 DIV 01 PRC 03', 'CMSA U09T1 PRC 01', 'CMSA U09T1 PRC 05', 'CMSA U11T2 DIV 01 PRC 01', 'CSSC O19T1 DIV 01 PRC 02', 'CMSA U08T1 DIV 01 PRC 05', 'CMSA U13T5 PRC 04', 'CMSA U13T4 DIV 02 PRC 04', 'CMSA U09T1 PRC 04', 'CMSA U10T1 DIV 01 PRC 01', 'CMSA U13T5 PRC 02', 'CMSA U14T3 PRC 04', 'CMSA U19T1 PRC 01', 'CMSA U13T3 PRC 02', 'CUSA O35T1 PRC 02', 'CMSA U07T1 DIV 01 PRC 04', 'CSSC O19T1 DIV 03 PRC 17', 'CUSA O19T1 PRC 02', 'CMSA U17T4 PRC 01', 'CMSA U11T1 DIV 01 PRC 04', 'CMSA U12T1 DIV 01 PRC 01', 'CMSA U15T2 PRC 01', 'CMSA U12T3 DIV 01 PRC 01', 'CMSA U13T2 PRC 01', 'CSSC O19T1 DIV 95 PRC 97', 'CMSA U12T4 DIV 01 PRC 01', 'CMSA U12T2 DIV 01 PRC 01', 'CMSA U10T1 DIV 01 PRC 04', 'CMSA U14T2 DIV 02 PRC 03', 'CMSA U12T3 DIV 01 PRC 02', 'CSSC O19T1 DIV 04 PRC 24', 'CMSA U12T1 DIV 01 PRC 03', 'CMSA U08T1 DIV 01 PRC 02', 'CMSA U16T3 PRC 01', 'CSSC O19T1 DIV 95 PRC 90', 'CMSA U13T1 DIV 01 PRC 01', 'CSSC O19T1 DIV 04 PRC 20', 'CMSA U13T4 DIV 02 PRC 05', 'CMSA U17T3 PRC 02', 'CMSA U14T1 PRC 02', 'CMSA U14T2 DIV 01 PRC 01', 'CMSA U14T4 DIV 01 PRC 02', 'CSSC O19T1 DIV 03 PRC 13', 'CMSA U08T1 DIV 01 PRC 06', 'CMSA U10T1 DIV 01 PRC 02', 'CMSA U13T1 DIV 01 PRC 03', 'CMSA U14T3 PRC 01', 'CSSC O19T1 DIV 04 PRC 21', 'CMSA U16T3 PRC 02', 'CMSA U08T1 DIV 01 PRC 03', 'CMSA U11T1 DIV 01 PRC 03', 'CMSA U19T2 PRC 01', 'CSSC O19T1 DIV 95 PRC 96', 'CSSC O19T1 DIV 02 PRC 11', 'CMSA U10T1 DIV 02 PRC 08', 'CSSC O19T1 DIV 95 PRC 95', 'CSSC O19T1 DIV 04 PRC 19', 'CMSA U19T4 PRC 01', 'CMSA U12T5 DIV 01 PRC 01', 'CMSA U08T1 DIV 01 PRC 04', 'CMSA U14T1 PRC 01', 'CMSA U19T1 PRC 02', 'CMSA U12T5 DIV 01 PRC 03', 'CSSC O19T1 DIV 01 PRC 01', 'CMSA U15T4 PRC 01', 'CUSA O19T1 PRC 03', 'CMSA U10T1 DIV 01 PRC 03', 'CSSC O19T1 DIV 02 PRC 09', 'CMSA U16T4 PRC 01', 'CSSC O19T1 DIV 01 PRC 06', 'CMSA U07T1 DIV 01 PRC 01', 'CMSA U12T5 DIV 01 PRC 04', 'CSSC O19T1 DIV 04 PRC 23', 'CMSA U13T1 DIV 01 PRC 02', 'CMSA U07T1 DIV 01 PRC 02', 'CMSA U13T3 PRC 01', 'CMSA U15T3 PRC 01', 'CMSA U12T3 DIV 01 PRC 03', 'CUSA O35T1 PRC 05', 'CMSA U07T1 DIV 01 PRC 03', 'CMSA U13T5 PRC 03', 'CMSA U19T3 PRC 01', 'CMSA U12T2 DIV 01 PRC 02', 'CSSC O19T1 DIV 03 PRC 14', 'CMSA U13T4 DIV 01 PRC 03', 'CMSA U10T1 DIV 02 PRC 06', 'CUSA O35T1 PRC 03', 'CMSA U14T4 DIV 01 PRC 01', 'CMSA U16T4 PRC 02', 'CSSC O19T1 DIV 03 PRC 15', 'CMSA U10T1 DIV 02 PRC 07', 'CSSC O19T1 DIV 01 PRC 05', 'CMSA U09T1 PRC 02', 'CMSA U19T3 PRC 02', 'CSSC O19T1 DIV 01 PRC 04', 'CSSC O19T1 DIV 03 PRC 16', 'CMSA U17T4 PRC 02', 'CMSA U14T4 DIV 01 PRC 04', 'CMSA U17T3 PRC 01', 'CMSA U12T5 DIV 01 PRC 02', 'CMSA U10T1 DIV 02 PRC 05', 'CSSC O19T1 DIV 02 PRC 07', 'CMSA U09T1 PRC 06', 'CMSA U09T1 PRC 03', 'CMSA U14T2 DIV 01 PRC 02', 'CUSA O35T1 PRC 04', 'CMSA U14T4 DIV 01 PRC 03', 'CMSA U16T2 PRC 01', 'CMSA U13T4 DIV 01 PRC 02', 'CMSA U12T1 DIV 01 PRC 02', 'CMSA U13T4 DIV 02 PRC 06', 'CUSA O19T1 PRC 01', 'CMSA U11T1 DIV 01 PRC 01', 'CSSC O19T1 DIV 02 PRC 10', 'CSSC O19T1 DIV 95 PRC 99', 'CMSA U13T4 DIV 01 PRC 01', 'CMSA U15T1 PRC 01', 'CMSA U17T2 PRC 02', 'CSSC O19T1 DIV 95 PRC 98', 'CMSA U11T1 DIV 01 PRC 02', 'CSSC O19T1 DIV 04 PRC 22'}
  Children Count: 0

CPSC433F24-LargeInput2.txt ->
Eval:  17905
Node at Depth 47:
  Parent Node Depth: 46
  Slot(Day=MO, StartTime=8:00, MaxGames=2, MinGames=1, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U10T1 DIV 01', 'CMSA U10T1 DIV 02'], AssignedPractices=[])
  Slot(Day=MO, StartTime=9:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CSSC O19T1 DIV 01', 'CSSC O19T1 DIV 02', 'CSSC O19T1 DIV 03', 'CSSC O19T1 DIV 04', 'CMSA U07T1 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=10:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U12T1 DIV 01', 'CMSA U12T5 DIV 
01', 'CMSA U15T2 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=11:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U10T2 DIV 01', 'CMSA U13T1 DIV 
01', 'CMSA U15T3 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=12:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U11T1 DIV 01', 'CMSA U13T2 DIV 
01', 'CMSA U15T4 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=13:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U11T2 DIV 01', 'CMSA U13T3 DIV 
01', 'CMSA U15T5 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=14:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U12T2 DIV 01', 'CMSA U13T4 DIV 
01', 'CMSA U13T4 DIV 02', 'CMSA U16T1 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=15:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U12T3 DIV 01', 'CMSA U13T5 DIV 
01', 'CMSA U16T2 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=16:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U12T4 DIV 01', 'CMSA U14T1 DIV 
01', 'CMSA U16T3 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=17:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U14T2 DIV 01', 'CMSA U14T2 DIV 
02', 'CMSA U17T2 DIV 01', 'CUSA O19T1 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=18:00, MaxGames=1, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CSSC O19T1 DIV 95'], AssignedPractices=[])
  Slot(Day=MO, StartTime=19:00, MaxGames=1, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U08T1 DIV 01'], AssignedPractices=[])
  Slot(Day=MO, StartTime=20:00, MaxGames=1, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U09T1 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=8:00, MaxGames=2, MinGames=1, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U14T3 DIV 01', 'CMSA U15T1 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=9:30, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U14T4 DIV 01', 'CMSA U16T4 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=11:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=12:30, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U17T3 DIV 01', 'CUSA O35T1 DIV 
01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=14:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U19T2 DIV 01', 'CUSA O35T1 DIV 
02'], AssignedPractices=[])
  Slot(Day=TU, StartTime=15:30, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U17T4 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=17:00, MaxGames=5, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U19T1 DIV 01'], AssignedPractices=[])
  Slot(Day=TU, StartTime=18:30, MaxGames=1, MinGames=0, MaxPractices=0, MinPractices=0, AssignedGames=['CMSA U09T1 DIV 02'], AssignedPractices=[])
  Slot(Day=MO, StartTime=8:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=1, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=9:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=10:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=11:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=12:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=13:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=14:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=15:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=16:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=17:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=18:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=19:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=MO, StartTime=20:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=8:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=1, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=9:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=10:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=11:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=12:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=13:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=14:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=15:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=16:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=17:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=3, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=18:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=['CMSA U12T1S', 
'CMSA U13T1S'])
  Slot(Day=TU, StartTime=19:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=TU, StartTime=20:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=8:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=10:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=12:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=14:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=16:00, MaxGames=0, MinGames=0, MaxPractices=6, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Slot(Day=FR, StartTime=18:00, MaxGames=0, MinGames=0, MaxPractices=2, MinPractices=0, AssignedGames=[], AssignedPractices=[])
  Remaining Games: {'CMSA U19T4 DIV 01', 'CMSA U19T3 DIV 01'}
  Remaining Practices: {'CMSA U12T2 DIV 01 PRC 02', 'CMSA U11T1 DIV 01 PRC 01', 'CMSA U17T3 PRC 02', 'CMSA U13T1 DIV 01 PRC 01', 'CSSC O19T1 DIV 03 PRC 17', 'CMSA U13T4 DIV 02 PRC 06', 'CUSA O35T1 PRC 03', 'CMSA U19T4 PRC 01', 'CSSC O19T1 DIV 01 PRC 04', 'CMSA U12T5 DIV 01 PRC 02', 'CMSA U07T1 DIV 01 PRC 02', 'CMSA U16T3 PRC 01', 'CMSA U07T1 DIV 01 PRC 04', 'CMSA U10T1 DIV 02 PRC 05', 'CMSA U08T1 DIV 01 PRC 01', 'CMSA U08T1 DIV 01 PRC 02', 'CMSA U15T4 PRC 01', 'CSSC O19T1 DIV 02 PRC 08', 'CMSA U09T1 PRC 06', 'CMSA U10T1 DIV 01 PRC 03', 'CMSA U14T4 DIV 01 PRC 01', 'CSSC O19T1 DIV 01 PRC 02', 'CMSA U14T3 PRC 03', 'CMSA U17T3 PRC 01', 'CSSC O19T1 DIV 95 PRC 96', 'CSSC O19T1 DIV 04 PRC 24', 'CSSC O19T1 DIV 02 PRC 11', 'CMSA U16T1 PRC 01', 'CSSC O19T1 DIV 95 PRC 90', 'CMSA U13T3 PRC 02', 'CMSA U13T1 DIV 01 PRC 02', 'CMSA U13T4 DIV 02 PRC 04', 'CMSA U13T3 PRC 01', 'CMSA U10T1 DIV 01 PRC 01', 'CMSA U09T1 PRC 05', 'CMSA U15T3 PRC 01', 'CSSC O19T1 DIV 02 PRC 09', 'CSSC O19T1 DIV 03 PRC 13', 'CMSA U12T4 DIV 01 PRC 01', 'CSSC O19T1 DIV 95 PRC 99', 'CMSA U16T4 PRC 01', 'CMSA U19T1 PRC 02', 'CMSA U14T3 PRC 02', 'CMSA U16T4 PRC 02', 'CMSA U09T1 PRC 01', 'CMSA U12T5 DIV 01 PRC 03', 'CMSA U16T3 PRC 02', 'CMSA U14T3 PRC 01', 'CMSA U13T1 DIV 01 PRC 03', 'CMSA U14T4 DIV 01 PRC 02', 'CMSA U14T2 DIV 01 PRC 02', 'CSSC O19T1 DIV 03 PRC 15', 'CMSA U14T4 DIV 01 PRC 04', 'CUSA O35T1 PRC 05', 'CMSA U07T1 DIV 01 PRC 03', 'CSSC O19T1 DIV 02 PRC 10', 'CUSA O35T1 PRC 02', 'CMSA U09T1 PRC 02', 'CSSC O19T1 DIV 03 PRC 14', 'CMSA U12T3 DIV 01 PRC 03', 'CMSA U12T5 DIV 01 PRC 01', 'CMSA U08T1 DIV 01 PRC 06', 'CSSC O19T1 DIV 04 PRC 19', 'CSSC O19T1 DIV 03 PRC 18', 'CMSA U10T1 DIV 02 PRC 07', 'CUSA O19T1 PRC 03', 'CMSA U13T5 PRC 01', 'CMSA U14T1 PRC 01', 'CMSA U12T1 DIV 01 PRC 02', 'CMSA U13T4 DIV 01 PRC 03', 'CMSA U14T2 DIV 02 PRC 04', 'CUSA O19T1 PRC 01', 'CMSA U11T1 DIV 01 PRC 02', 'CMSA U14T2 DIV 01 PRC 01', 'CMSA U12T5 DIV 01 PRC 04', 'CMSA U13T4 DIV 02 PRC 05', 'CSSC O19T1 DIV 02 PRC 07', 'CSSC O19T1 DIV 04 PRC 21', 'CMSA U15T5 PRC 01', 'CMSA U15T2 PRC 01', 'CMSA U16T2 PRC 01', 'CMSA U07T1 DIV 01 PRC 01', 'CSSC O19T1 DIV 04 PRC 22', 'CSSC O19T1 DIV 04 PRC 20', 'CMSA U13T5 PRC 02', 'CMSA U15T1 PRC 01', 'CMSA U19T2 PRC 01', 'CMSA U17T2 PRC 01', 'CSSC O19T1 DIV 95 PRC 95', 'CMSA U12T3 DIV 01 PRC 02', 'CMSA U09T1 PRC 07', 'CMSA U12T3 DIV 01 PRC 01', 'CMSA U13T4 DIV 01 PRC 02', 'CSSC O19T1 DIV 03 PRC 16', 'CSSC O19T1 DIV 01 PRC 01', 'CMSA U10T1 DIV 01 PRC 04', 'CMSA U10T1 DIV 02 PRC 06', 'CMSA U13T5 PRC 04', 'CMSA U17T4 PRC 01', 'CSSC O19T1 DIV 95 PRC 98', 'CSSC O19T1 DIV 01 PRC 06', 'CUSA O35T1 PRC 01', 'CMSA U17T4 PRC 02', 'CMSA U11T1 DIV 01 PRC 03', 'CMSA U08T1 DIV 01 PRC 03', 'CMSA U12T2 DIV 01 PRC 01', 'CMSA U19T3 PRC 01', 'CMSA U08T1 DIV 01 PRC 05', 'CMSA U14T1 PRC 02', 'CMSA U14T3 PRC 04', 'CMSA U10T1 DIV 01 PRC 02', 'CSSC O19T1 DIV 02 PRC 12', 'CMSA U12T1 DIV 01 PRC 03', 'CSSC O19T1 DIV 01 PRC 03', 'CMSA U10T1 DIV 02 PRC 08', 'CSSC O19T1 DIV 95 PRC 97', 'CMSA U14T2 DIV 02 PRC 03', 'CMSA U13T4 DIV 01 PRC 01', 'CMSA U11T1 DIV 01 PRC 04', 'CMSA U12T1 DIV 01 PRC 01', 'CSSC O19T1 DIV 04 PRC 23', 'CMSA U17T2 PRC 02', 'CMSA U19T3 PRC 02', 'CUSA O35T1 PRC 04', 'CSSC O19T1 DIV 01 PRC 05', 'CMSA U13T2 PRC 01', 'CMSA U09T1 PRC 04', 'CMSA U08T1 DIV 01 PRC 04', 'CMSA U13T5 PRC 03', 'CMSA U14T4 DIV 01 PRC 03', 'CMSA U19T1 PRC 01', 'CMSA U11T2 DIV 01 PRC 01', 'CMSA U09T1 PRC 03', 'CUSA O19T1 PRC 02'}
  Children Count: 0