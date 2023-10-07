from todo import hello_world

def test_hello_world(capsys):
    hello_world('Gerald')
    captured_prints = capsys.readouterr()
    assert captured_prints.out == 'Hello Gerald!'
