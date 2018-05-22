# :biohazard: ePydemic

**Assignment for INE5425@UFSC** :brazil:

ePydemic implements a celullar automaton for epidemic disease simulation based on (G. MELOTTI, 2009) using Python and Qt.

## Usage

---

GUI version:

```console
/ePydemic
$./run.sh epydemic
```

CLI version using specific parameters to compare against (MELOTTI, 2009):

```console
/ePydemic
$./run.sh epydemic-compare
```

## When things go wrong...

---

### **No such file or directory**

If something goes wrong during the creation of the virtual environment, some files and dependencies might not get installed.

```console
$./run.sh epydemic
./run.sh: line 12: .venv/bin/epydemic: No such file or directory
```

Make sure to delete **.venv/** before running the script again.

### **No module named 'tkinter'**

`ModuleNotFoundError: No module named 'tkinter'`

This error is caused by an external dependency of _matplotlib_.

On Debian/Ubuntu based systems:

```console
$sudo apt-get install python3-tk
```

---

## Bibliography:

* G. MELOTTI. 2009. ["Aplicação de Autômatos Celulares em Sistemas Complexos: Um Estudo de Caso em Espalhamento de Epidemias."](https://www.ppgee.ufmg.br/documentos/Defesas/802/Dissertacao_Gledson_final.pdf) Universidade Federal de Minas Gerais.
