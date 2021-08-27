from flask import Flask, request

app = Flask(__name__)




@app.route('/',methods=['GET','POST'])
def buttons1():
    if request.method == 'GET':
        return startpage1.format(0,1000)
    else:
        min = int(request.form.get("min"))
        max = int(request.form.get("max"))
        user_answer = request.form.get('user_answer')
        guess = int(request.form.get("guess", 500))

        if user_answer == "too big":
            max = guess
        elif user_answer == "too low":
            min = guess
        elif user_answer == "correct":
            return finalpage.format(guess=guess)

        guess = (max - min) // 2 + min

        return mainpage.format(guess=guess,min=min, max=max)




startpage1 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guess the number</title>
</head>
<body>
<h1>Imagine number from 0 to 1000</h1>
<h2>I'm going to guess the number in maximum 10 moves</h2>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}">
    <input type="hidden" name="max" value="{}">
    <input type="submit" value="OK, lets start">
</form>
</body>
</html>
"""

mainpage = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Main page, guess the number</title>
</head>
<body>
<h1>It is the number <strong>{guess}</strong>?</h1>
<form action="" method="POST">
    <input type='submit' value="too big" name='user_answer'>
    <input type='submit' value="too low" name='user_answer'>
    <input type='submit' value="correct" name='user_answer'>
    <input type="hidden" name="min" value="{min}">
    <input type="hidden" name="max" value="{max}">
    <input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
"""

finalpage = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>guess the number</title>
</head>
<body>
<h1>your number is {guess}</h1>
</body>
</html>
"""

if __name__ == '__main__':
    app.run()