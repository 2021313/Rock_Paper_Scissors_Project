from io import StringIO
from R_P_S_Play_First import Get_Player_Name
name_input = StringIO('Devon')
def test_Get_Player_Name(monkeypatch):
    monkeypatch.setattr('sys.stdin', name_input)
    assert Get_Player_Name() == 'Devon'