from beaker import *
from pyteal import *

app = Application("HelloWorld")


@app.external
def hello(name: abi.String, *, output: abi.String) -> Expr:
    return output.set(Concat(Bytes("Hello, "), name.get()))


@app.external
def addString(a: abi.String, b: abi.String, *, output: abi.String) -> Expr:
    return output.set(Concat(a.get(), b.get()))


@app.external
def addCalc(a: abi.Uint64, b: abi.Uint64, *, output: abi.Uint64) -> Expr:
    return output.set(a.get() + b.get())


# if b value is greater tha a value it will through error
@app.external
def subCalc(a: abi.Uint64, b: abi.Uint64, *, output: abi.Uint64) -> Expr:
    return output.set(a.get() - b.get())


@app.external
def difference(a: abi.Uint64, b: abi.Uint64, *, output: abi.Uint64) -> Expr:
    return (
        If(a.get() > b.get())
        .Then(output.set(a.get() - b.get()))
        .Else(output.set(b.get() - a.get()))
    )


@app.external
def logger(a: abi.String, b: abi.String, *, output: abi.String) -> Expr:
    return Seq(Log(a.get()), Log(b.get()), output.set(Concat(a.get(), b.get())))


@app.delete(bare=True, authorize=Authorize.only(Global.creator_address()))
def delete() -> Expr:
    return Approve()


if __name__ == "__main__":
    app.build().export("./artifacts")
