##### Signed by https://keybase.io/clcollins
```
-----BEGIN PGP SIGNATURE-----
Version: GnuPG v1

iEYEABECAAYFAlRmgxEACgkQte6EFif3vzcI8gCg+xtsv6o0b1mcUD34w+7/Uxp2
I+kAn2fr2wz55Wy90mL5IVGC5D1aNuRt
=j2iA
-----END PGP SIGNATURE-----

```

<!-- END SIGNATURES -->

### Begin signed statement 

#### Expect

```
size   exec  file               contents                                                                                                                         
             ./                                                                                                                                                  
               .ropeproject/                                                                                                                                     
3461             config.py      ce4bf771a9bf21db900ea0097013f94178e101192d6990baf1618a1b7bdfd3d4                                                                 
6                globalnames    e9aeccf6ac0589767985fd99de8fcac1004521a30a4c46d5a62ed4f19476a52b|b72bc82dae0d8bd11c7734208b99c08cd2c86acbc5728316eccb18a405880ad6
14               history        6bae52695804b23d13199e198b5d2b4ddad85715b6e3e789d61179a73130dbcf|b4c4897ff898e5b3aa46aa52c6b7589eee655dbf13dd0ff183691c5e34b1669b
1174             objectdb       9976794f7c36a78b2b7e8f8fd63eb652d05faf16d69903eb607f24d8fa066be2|a9ea2915dd88332dbfe6a9ed2df517a701ddf90c53996230e5ccce9db9cf87d9
226            Dockerfile       e55d7796708f7b1037070272774632fbd45565652d8451e939cd98a7d6a4694d                                                                 
35121          LICENSE          e1c0ad728983d8a57335e52cf1064f1affd1d454173d8cebd3ed8b4a72b48704                                                                 
958    x       mysql-backup.py  829fad33fc4e464afc291d290383db8aa4caf3b62d85d74da1a374ab22ffa9cb                                                                 
```

#### Ignore

```
/SIGNED.md
```

#### Presets

```
git      # ignore .git and anything as described by .gitignore files
dropbox  # ignore .dropbox-cache and other Dropbox-related files    
kb       # ignore anything as described by .kbignore files          
```

<!-- summarize version = 0.0.9 -->

### End signed statement

<hr>

#### Notes

With keybase you can sign any directory's contents, whether it's a git repo,
source code distribution, or a personal documents folder. It aims to replace the drudgery of:

  1. comparing a zipped file to a detached statement
  2. downloading a public key
  3. confirming it is in fact the author's by reviewing public statements they've made, using it

All in one simple command:

```bash
keybase dir verify
```

There are lots of options, including assertions for automating your checks.

For more info, check out https://keybase.io/docs/command_line/code_signing