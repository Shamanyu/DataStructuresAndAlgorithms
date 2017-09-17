#@/bin/bash

if [["$email" =~ "^[A-Za-z0-9._%+_]+<b>@</b>[A-Za-z0-9.-]+<b>\.</b>[A-Za-z]{2,4}$" ]]
then
	echo "This email address looks fine: $email"
else
	echo "This email address is flawed: $email"
fi
