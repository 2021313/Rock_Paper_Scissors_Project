from io import StringIO
from R_P_S_Play_First import Get_Player_Name
from R_P_S_Play_First import Pick_First_Player

name_input = StringIO('Devon\n')

def test_Get_Player_Name(monkeypatch):
    monkeypatch.setattr('sys.stdin', name_input)
    assert Get_Player_Name() == 'Devon'

def test_Pick_First_Player():
    p1, p2 = Pick_First_Player('Devon', 'Tara')
    assert (p1 == 'Devon' and p2 == 'Tara') or (p1 == 'Tara' and p2 == 'Devon')