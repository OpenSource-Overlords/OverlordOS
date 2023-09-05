import subprocess

def test_hello_world():
    result = subprocess.run(['python', 'hello.py'], capture_output=True, text=True)
    output = result.stdout.strip()  # This gets the output and removes any leading/trailing whitespaces.
    
    assert output == "Hello, World!", f"Expected 'Hello, World!' but got '{output}'"

    #blah blah blah this is an if statement doi

    #eyy this is a comment in a test classsssssssss
if __name__ == "__main__":
    test_hello_world()
    print("All tests passed!")

print('This is a test file')
