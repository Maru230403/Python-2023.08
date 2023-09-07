{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "계좌번호:230906, 소유주:제임스, 잔액:   100,000\n",
      "계좌번호:230906, 소유주:제임스, 잔액:   300,000\n"
     ]
    },
    {
     "ename": "AttributeError",
     "evalue": "'Account' object has no attribute 'withdraw'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 29\u001b[0m\n\u001b[0;32m     27\u001b[0m acc\u001b[39m.\u001b[39mdeposit(\u001b[39m200000\u001b[39m)\n\u001b[0;32m     28\u001b[0m \u001b[39mprint\u001b[39m(acc)\n\u001b[1;32m---> 29\u001b[0m acc\u001b[39m.\u001b[39mwithdraw(\u001b[39m400000\u001b[39m)\n\u001b[0;32m     30\u001b[0m acc\u001b[39m.\u001b[39mwithdraw(\u001b[39m250000\u001b[39m)\n\u001b[0;32m     31\u001b[0m \u001b[39mprint\u001b[39m(acc)\n",
      "\u001b[1;31mAttributeError\u001b[0m: 'Account' object has no attribute 'withdraw'"
     ]
    }
   ],
   "source": [
    "# 센세 풀이\n",
    "class Account:\n",
    "    def __init__(self, ano, owner, balance):\n",
    "        self.ano = ano\n",
    "        self.owner = owner\n",
    "        self.balance = 0\n",
    "        if 0 <= balance <= 100000000:\n",
    "            self.balance = balance\n",
    "        # else:\n",
    "        #    self.balance = 0\n",
    "    def deposit(self, amount):\n",
    "        if self.balance + amount > 10000000:\n",
    "            print('일천만원이 초과할 수 없습니다.')\n",
    "            return\n",
    "        self.balance += amount\n",
    "    def wuthdraw(self, amount):\n",
    "        if self.balance < amount:\n",
    "            print('잔액이 부족합니다.')\n",
    "            return\n",
    "        self.balance -= amount\n",
    "    def __str__(self):\n",
    "        return f'계좌번호:{self.ano}, 소유주:{self.owner}, 잔액:{self.balance:10,d}'\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    acc = Account('230906', '제임스', 100000)\n",
    "    print(acc)\n",
    "    acc.deposit(200000)\n",
    "    print(acc)\n",
    "    acc.withdraw(400000)\n",
    "    acc.withdraw(250000)\n",
    "    print(acc)\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
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
   "version": "3.11.4"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
