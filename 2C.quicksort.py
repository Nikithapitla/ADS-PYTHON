{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "protecting-impression",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the list of numbers: 4 5 3 6 2 \n",
      "Sorted list: [2, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "def quicksort(arr, start, end):\n",
    "    \n",
    "    if end - start > 1:\n",
    "        p = partition(arr, start, end)\n",
    "        quicksort(arr, start, p)\n",
    "        quicksort(arr, p + 1, end)\n",
    " \n",
    " \n",
    "def partition(arr, start, end):\n",
    "    pivot = arr[start]\n",
    "    i = start + 1\n",
    "    j = end - 1\n",
    " \n",
    "    while True:\n",
    "        while (i <= j and arr[i] <= pivot):\n",
    "            i = i + 1\n",
    "        while (i <= j and arr[j] >= pivot):\n",
    "            j = j - 1\n",
    " \n",
    "        if i <= j:\n",
    "            arr[i], arr[j] = arr[j], arr[i]\n",
    "        else:\n",
    "            arr[start], arr[j] = arr[j], arr[start]\n",
    "            return j\n",
    " \n",
    " \n",
    "arr = input('Enter the list of numbers: ').split()\n",
    "arr = [int(x) for x in arr]\n",
    "quicksort(arr, 0, len(arr))\n",
    "print('Sorted list: ', end='')\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "relevant-thesis",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "powered-drink",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "valued-arkansas",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "russian-victoria",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "executive-malaysia",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
