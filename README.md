# skymap_python CLI
command line interface for astronomy use 
you can perform astronomic calculations using this interface

### example az and alt of star based on your position

    python3 skymap.py calculate-all [latitude] [longitude] [Dec] [Ra] [year] [month] [day] [utc]
    los angeles and sirius example:
    python3 skymap.py calculate-all 34.052235 -118.243683 -16.7424 101.52 2021 9 4 20
    
### days since j2000

    python3 skymap.py calculate-j2000 [year] [month] [day] [time_utc]
    usage:
    python3 skymap.py calculate-j2000 2021 9 12 12.50

### find star using database
    example syntax:
    python3 skymap.py search [Nameofstar] 
    or 
    python3 skymap.py -search [Nameofstar]
    example usage:
    python3 skymap.py search Sirius   
    
### step 1
    find Ra and Dec of your star on database or here 
            example syntax:
            python3 skymap.py search [Nameofstar] 
            or 
            python3 skymap.py -search [Nameofstar]
            example usage:
            python3 skymap.py search Sirius
### step 2
    python3 skymap.py calculate-all [latitude] [longitude] [Dec] [Ra] [year] [month] [day] [utc]
    los angeles and sirius example:
    python3 skymap.py calculate-all 34.052235 -118.243683 -16.7424 101.52 2021 9 4 20


