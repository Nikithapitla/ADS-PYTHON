{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "alone-bangladesh",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the list of numbers: 5 6 4 3 78\n",
      "Sorted list: [3, 4, 5, 6, 78]\n"
     ]
    }
   ],
   "source": [
    "def mergesort(arr, start, end):\n",
    "    \n",
    "    if end - start > 1:\n",
    "        mid = (start + end)//2\n",
    "        mergesort(arr, start, mid)\n",
    "        mergesort(arr, mid, end)\n",
    "        merge_list(arr, start, mid, end)\n",
    " \n",
    "def merge_list(arr, start, mid, end):\n",
    "    left = arr[start:mid]\n",
    "    right = arr[mid:end]\n",
    "    k = start\n",
    "    i = 0\n",
    "    j = 0\n",
    "    while (start + i < mid and mid + j < end):\n",
    "        if (left[i] <= right[j]):\n",
    "            arr[k] = left[i]\n",
    "            i = i + 1\n",
    "        else:\n",
    "            arr[k] = right[j]\n",
    "            j = j + 1\n",
    "        k = k + 1\n",
    "    if start + i < mid:\n",
    "        while k < end:\n",
    "            arr[k] = left[i]\n",
    "            i = i + 1\n",
    "            k = k + 1\n",
    "    else:\n",
    "        while k < end:\n",
    "            arr[k] = right[j]\n",
    "            j = j + 1\n",
    "            k = k + 1\n",
    " \n",
    " \n",
    "arr = input('Enter the list of numbers: ').split()\n",
    "arr = [int(x) for x in arr]\n",
    "mergesort(arr, 0, len(arr))\n",
    "print('Sorted list: ', end='')\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "broken-absolute",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "referenced-saver",
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
