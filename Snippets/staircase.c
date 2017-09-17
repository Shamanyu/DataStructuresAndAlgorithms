void staircase(int n)
{
    int counter, hashes, spaces;
    for(counter = 1; counter <= n counter++)
    {
        hashes = counter;
        spaces = n - hashes; 
        while(spaces > 0)
        {
            printf(" ");
            spaces --;
        }
        while(hashes > 0)
        {
            printf("#");
            hashes --;
        }
    }
}
    
