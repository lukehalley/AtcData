contract Contract {
    function main() {
        memory[0x40:0x60] = 0x80;
        var var0 = msg.value;
    
        if (var0) { revert(memory[0x00:0x00]); }
    
        if (msg.data.length < 0x04) { revert(memory[0x00:0x00]); }
    
        var0 = msg.data[0x00:0x20] >> 0xe0;
    
        if (0x9aab9248 > var0) {
            if (var0 == 0x017e7e58) {
                // Dispatch table entry for feeTo()
                var var1 = 0x00b0;
                var var2 = feeTo();
            
            label_00B0:
                var temp0 = memory[0x40:0x60];
                memory[temp0:temp0 + 0x20] = var2 & 0xffffffffffffffffffffffffffffffffffffffff;
                var temp1 = memory[0x40:0x60];
                return memory[temp1:temp1 + temp0 - temp1 + 0x20];
            } else if (var0 == 0x094b7415) {
                // Dispatch table entry for feeToSetter()
                var1 = 0x00b0;
                var2 = feeToSetter();
                goto label_00B0;
            } else if (var0 == 0x1e3dd18b) {
                // Dispatch table entry for allPairs(uint256)
                var1 = 0x00b0;
                var2 = 0x04;
                var var3 = msg.data.length - var2;
            
                if (var3 < 0x20) { revert(memory[0x00:0x00]); }
            
                var2 = allPairs(var2, var3);
                goto label_00B0;
            } else if (var0 == 0x574f2ba3) {
                // Dispatch table entry for allPairsLength()
                var1 = 0x0106;
                var1 = allPairsLength();
            
            label_0106:
                var temp2 = memory[0x40:0x60];
                memory[temp2:temp2 + 0x20] = var1;
                var temp3 = memory[0x40:0x60];
                return memory[temp3:temp3 + temp2 - temp3 + 0x20];
            } else { revert(memory[0x00:0x00]); }
        } else if (0xc9c65396 > var0) {
            if (var0 == 0x9aab9248) {
                // Dispatch table entry for pairCodeHash()
                var1 = 0x0106;
                var1 = pairCodeHash();
                goto label_0106;
            } else if (var0 == 0xa2e74af6) {
                // Dispatch table entry for setFeeToSetter(address)
                var1 = 0x0153;
                var2 = 0x04;
                var3 = msg.data.length - var2;
            
                if (var3 < 0x20) { revert(memory[0x00:0x00]); }
            
                setFeeToSetter(var2, var3);
                stop();
            } else { revert(memory[0x00:0x00]); }
        } else if (var0 == 0xc9c65396) {
            // Dispatch table entry for createPair(address,address)
            var1 = 0x00b0;
            var2 = 0x04;
            var3 = msg.data.length - var2;
        
            if (var3 < 0x40) { revert(memory[0x00:0x00]); }
        
            var1 = createPair(var2, var3);
            goto label_00B0;
        } else if (var0 == 0xe6a43905) {
            // Dispatch table entry for getPair(address,address)
            var1 = 0x00b0;
            var2 = 0x04;
            var3 = msg.data.length - var2;
        
            if (var3 < 0x40) { revert(memory[0x00:0x00]); }
        
            var2 = getPair(var2, var3);
            goto label_00B0;
        } else if (var0 == 0xf46901ed) {
            // Dispatch table entry for setFeeTo(address)
            var1 = 0x0153;
            var2 = 0x04;
            var3 = msg.data.length - var2;
        
            if (var3 < 0x20) { revert(memory[0x00:0x00]); }
        
            setFeeTo(var2, var3);
            stop();
        } else { revert(memory[0x00:0x00]); }
    }
    
    function allPairs(var arg0, var arg1) returns (var arg0) {
        arg0 = msg.data[arg0:arg0 + 0x20];
        arg1 = 0x03;
        var var0 = arg0;
    
        if (var0 >= storage[arg1]) { assert(); }
    
        memory[0x00:0x20] = arg1;
        return storage[keccak256(memory[0x00:0x20]) + var0] & 0xffffffffffffffffffffffffffffffffffffffff;
    }
    
    function setFeeToSetter(var arg0, var arg1) {
        arg0 = msg.data[arg0:arg0 + 0x20] & 0xffffffffffffffffffffffffffffffffffffffff;
    
        if (msg.sender == storage[0x01] & 0xffffffffffffffffffffffffffffffffffffffff) {
            storage[0x01] = (arg0 & 0xffffffffffffffffffffffffffffffffffffffff) | (storage[0x01] & 0xffffffffffffffffffffffff0000000000000000000000000000000000000000);
            return;
        } else {
            var temp0 = memory[0x40:0x60];
            memory[temp0:temp0 + 0x20] = 0x08c379a000000000000000000000000000000000000000000000000000000000;
            memory[temp0 + 0x04:temp0 + 0x04 + 0x20] = 0x20;
            memory[temp0 + 0x24:temp0 + 0x24 + 0x20] = 0x14;
            memory[temp0 + 0x44:temp0 + 0x44 + 0x20] = 0x556e697377617056323a20464f5242494444454e000000000000000000000000;
            var temp1 = memory[0x40:0x60];
            revert(memory[temp1:temp1 + temp0 - temp1 + 0x64]);
        }
    }
    
    function createPair(var arg0, var arg1) returns (var r0) {
        var temp0 = arg0;
        arg0 = msg.data[temp0:temp0 + 0x20] & 0xffffffffffffffffffffffffffffffffffffffff;
        arg1 = msg.data[temp0 + 0x20:temp0 + 0x20 + 0x20] & 0xffffffffffffffffffffffffffffffffffffffff;
        var var0 = 0x00;
    
        if (arg0 & 0xffffffffffffffffffffffffffffffffffffffff != arg1 & 0xffffffffffffffffffffffffffffffffffffffff) {
            var var1 = 0x00;
            var var2 = var1;
        
            if (arg0 & 0xffffffffffffffffffffffffffffffffffffffff < arg1 & 0xffffffffffffffffffffffffffffffffffffffff) {
                var1 = arg0;
                var2 = arg1;
            
                if (var1 & 0xffffffffffffffffffffffffffffffffffffffff) {
                label_04D3:
                    memory[0x00:0x20] = var1 & 0xffffffffffffffffffffffffffffffffffffffff;
                    memory[0x20:0x40] = 0x02;
                    var temp1 = keccak256(memory[0x00:0x40]);
                    memory[0x00:0x20] = var2 & 0xffffffffffffffffffffffffffffffffffffffff;
                    memory[0x20:0x40] = temp1;
                
                    if (!(storage[keccak256(memory[0x00:0x40])] & 0xffffffffffffffffffffffffffffffffffffffff)) {
                        var var3 = 0x60;
                        var var4 = memory[0x40:0x60];
                        var var5 = 0x0586;
                        var var6 = var4 + 0x20;
                        var5 = func_08A3(var6);
                        var temp2 = var4;
                        var temp3 = var5;
                        memory[temp2:temp2 + 0x20] = temp3 - (temp2 + 0x20);
                        memory[0x40:0x60] = temp3 + 0x1f & ~0x1f;
                        var3 = temp2;
                        var temp4 = var1;
                        var temp5 = var2;
                        var temp6 = memory[0x40:0x60] + 0x20;
                        memory[temp6:temp6 + 0x20] = (temp4 & 0xffffffffffffffffffffffffffffffffffffffff) << 0x60;
                        var temp7 = temp6 + 0x14;
                        memory[temp7:temp7 + 0x20] = (temp5 & 0xffffffffffffffffffffffffffffffffffffffff) << 0x60;
                        var temp8 = temp7 + 0x14;
                        var temp9 = memory[0x40:0x60];
                        memory[temp9:temp9 + 0x20] = temp8 - temp9 - 0x20;
                        memory[0x40:0x60] = temp8;
                        var4 = keccak256(memory[temp9 + 0x20:temp9 + 0x20 + memory[temp9:temp9 + 0x20]]);
                        var temp10 = new(memory[var3 + 0x20:var3 + 0x20 + memory[var3:var3 + 0x20]]).value(0x00).salt(var4)();
                        var0 = temp10;
                        var5 = var0 & 0xffffffffffffffffffffffffffffffffffffffff;
                        var6 = 0x485cc955;
                        var temp11 = memory[0x40:0x60];
                        memory[temp11:temp11 + 0x20] = (var6 & 0xffffffff) << 0xe0;
                        var temp12 = temp11 + 0x04;
                        memory[temp12:temp12 + 0x20] = temp4 & 0xffffffffffffffffffffffffffffffffffffffff;
                        var temp13 = temp12 + 0x20;
                        memory[temp13:temp13 + 0x20] = temp5 & 0xffffffffffffffffffffffffffffffffffffffff;
                        var var7 = temp13 + 0x20;
                        var var8 = 0x00;
                        var var9 = memory[0x40:0x60];
                        var var10 = var7 - var9;
                        var var11 = var9;
                        var var12 = 0x00;
                        var var13 = var5;
                        var var14 = !address(var13).code.length;
                    
                        if (var14) { revert(memory[0x00:0x00]); }
                    
                        var temp14;
                        temp14, memory[var9:var9 + var8] = address(var13).call.gas(msg.gas).value(var12)(memory[var11:var11 + var10]);
                        var8 = !temp14;
                    
                        if (!var8) {
                            var temp15 = var1 & 0xffffffffffffffffffffffffffffffffffffffff;
                            memory[0x00:0x20] = temp15;
                            memory[0x20:0x40] = 0x02;
                            var temp16 = keccak256(memory[0x00:0x40]);
                            var temp17 = var2 & 0xffffffffffffffffffffffffffffffffffffffff;
                            memory[0x00:0x20] = temp17;
                            memory[0x20:0x40] = temp16;
                            var temp18 = keccak256(memory[0x00:0x40]);
                            var temp19 = var0 & 0xffffffffffffffffffffffffffffffffffffffff;
                            storage[temp18] = temp19 | (storage[temp18] & 0xffffffffffffffffffffffff0000000000000000000000000000000000000000);
                            memory[0x20:0x40] = 0x02;
                            var temp20 = keccak256(memory[0x00:0x40]);
                            memory[0x00:0x20] = temp15;
                            memory[0x20:0x40] = temp20;
                            var temp21 = keccak256(memory[0x00:0x40]);
                            storage[temp21] = temp19 | (storage[temp21] & 0xffffffffffffffffffffffff0000000000000000000000000000000000000000);
                            var temp22 = storage[0x03];
                            storage[0x03] = temp22 + 0x01;
                            memory[0x00:0x20] = 0x03;
                            var temp23 = temp22 + 0xc2575a0e9e593c00f959f8c92f12db2869c3395a3b0502d05e2516446f71f85b;
                            storage[temp23] = temp19 | (storage[temp23] & 0xffffffffffffffffffffffff0000000000000000000000000000000000000000);
                            var temp24 = memory[0x40:0x60];
                            memory[temp24:temp24 + 0x20] = temp19;
                            memory[temp24 + 0x20:temp24 + 0x20 + 0x20] = storage[0x03];
                            var temp25 = memory[0x40:0x60];
                            log(memory[temp25:temp25 + temp24 - temp25 + 0x40], [0x0d3648bd0f6ba80134a33ba9275ac585d9d315f0ad8355cddefde31afa28d0e9, stack[-8] & 0xffffffffffffffffffffffffffffffffffffffff, stack[-7] & 0xffffffffffffffffffffffffffffffffffffffff]);
                            return var0;
                        } else {
                            var temp26 = returndata.length;
                            memory[0x00:0x00 + temp26] = returndata[0x00:0x00 + temp26];
                            revert(memory[0x00:0x00 + returndata.length]);
                        }
                    } else {
                        var temp27 = memory[0x40:0x60];
                        memory[temp27:temp27 + 0x20] = 0x08c379a000000000000000000000000000000000000000000000000000000000;
                        memory[temp27 + 0x04:temp27 + 0x04 + 0x20] = 0x20;
                        memory[temp27 + 0x24:temp27 + 0x24 + 0x20] = 0x16;
                        memory[temp27 + 0x44:temp27 + 0x44 + 0x20] = 0x556e697377617056323a20504149525f45584953545300000000000000000000;
                        var temp28 = memory[0x40:0x60];
                        revert(memory[temp28:temp28 + temp27 - temp28 + 0x64]);
                    }
                } else {
                label_046D:
                    var temp29 = memory[0x40:0x60];
                    memory[temp29:temp29 + 0x20] = 0x08c379a000000000000000000000000000000000000000000000000000000000;
                    memory[temp29 + 0x04:temp29 + 0x04 + 0x20] = 0x20;
                    memory[temp29 + 0x24:temp29 + 0x24 + 0x20] = 0x17;
                    memory[temp29 + 0x44:temp29 + 0x44 + 0x20] = 0x556e697377617056323a205a45524f5f41444452455353000000000000000000;
                    var temp30 = memory[0x40:0x60];
                    revert(memory[temp30:temp30 + temp29 - temp30 + 0x64]);
                }
            } else {
                var3 = arg1;
                var4 = arg0;
                var1 = var3;
                var2 = var4;
            
                if (var1 & 0xffffffffffffffffffffffffffffffffffffffff) { goto label_04D3; }
                else { goto label_046D; }
            }
        } else {
            var temp31 = memory[0x40:0x60];
            memory[temp31:temp31 + 0x20] = 0x08c379a000000000000000000000000000000000000000000000000000000000;
            memory[temp31 + 0x04:temp31 + 0x04 + 0x20] = 0x20;
            memory[temp31 + 0x24:temp31 + 0x24 + 0x20] = 0x1e;
            memory[temp31 + 0x44:temp31 + 0x44 + 0x20] = 0x556e697377617056323a204944454e544943414c5f4144445245535345530000;
            var temp32 = memory[0x40:0x60];
            revert(memory[temp32:temp32 + temp31 - temp32 + 0x64]);
        }
    }
    
    function getPair(var arg0, var arg1) returns (var arg0) {
        var temp0 = arg0;
        arg0 = msg.data[temp0:temp0 + 0x20] & 0xffffffffffffffffffffffffffffffffffffffff;
        arg1 = msg.data[temp0 + 0x20:temp0 + 0x20 + 0x20] & 0xffffffffffffffffffffffffffffffffffffffff;
        memory[0x20:0x40] = 0x02;
        memory[0x00:0x20] = arg0;
        memory[0x20:0x40] = keccak256(memory[0x00:0x40]);
        memory[0x00:0x20] = arg1;
        return storage[keccak256(memory[0x00:0x40])] & 0xffffffffffffffffffffffffffffffffffffffff;
    }
    
    function setFeeTo(var arg0, var arg1) {
        arg0 = msg.data[arg0:arg0 + 0x20] & 0xffffffffffffffffffffffffffffffffffffffff;
    
        if (msg.sender == storage[0x01] & 0xffffffffffffffffffffffffffffffffffffffff) {
            storage[0x00] = (arg0 & 0xffffffffffffffffffffffffffffffffffffffff) | (storage[0x00] & 0xffffffffffffffffffffffff0000000000000000000000000000000000000000);
            return;
        } else {
            var temp0 = memory[0x40:0x60];
            memory[temp0:temp0 + 0x20] = 0x08c379a000000000000000000000000000000000000000000000000000000000;
            memory[temp0 + 0x04:temp0 + 0x04 + 0x20] = 0x20;
            memory[temp0 + 0x24:temp0 + 0x24 + 0x20] = 0x14;
            memory[temp0 + 0x44:temp0 + 0x44 + 0x20] = 0x556e697377617056323a20464f5242494444454e000000000000000000000000;
            var temp1 = memory[0x40:0x60];
            revert(memory[temp1:temp1 + temp0 - temp1 + 0x64]);
        }
    }
    
    function feeTo() returns (var r0) { return storage[0x00] & 0xffffffffffffffffffffffffffffffffffffffff; }
    
    function feeToSetter() returns (var r0) { return storage[0x01] & 0xffffffffffffffffffffffffffffffffffffffff; }
    
    function allPairsLength() returns (var r0) { return storage[0x03]; }
    
    function pairCodeHash() returns (var r0) {
        var var0 = 0x00;
        var var1 = memory[0x40:0x60];
        var var3 = var1 + 0x20;
        var var2 = 0x0282;
        var2 = func_08A3(var3);
        var temp0 = var1;
        var temp1 = var2;
        memory[temp0:temp0 + 0x20] = temp1 - (temp0 + 0x20);
        memory[0x40:0x60] = temp1 + 0x1f & ~0x1f;
        return keccak256(memory[temp0 + 0x20:temp0 + 0x20 + memory[temp0:temp0 + 0x20]]);
    }
    
    function func_08A3(var arg0) returns (var r0) {
        var temp0 = arg0;
        memory[temp0:temp0 + 0x2c5d] = code[0x08b1:0x350e];
        return temp0 + 0x2c5d;
    }
}