from ctypes import CFUNCTYPE, c_int
import sys
import llvmlite.ir as ll
import llvmlite.binding as llvm

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

module = ll.Module()
func_ty = ll.FunctionType(ll.IntType(32), [ll.IntType(32), ll.IntType(32)])
func = ll.Function(module, func_ty, name="sum")

func.args[0].name = 'a'
func.args[1].name = 'b'

bb_entry = func.append_basic_block('entry')
irbuilder = ll.IRBuilder(bb_entry)
tmp = irbuilder.add(func.args[0], func.args[1])
ret = irbuilder.ret(tmp)

print('====== LLVM IR')
print(module)

llvm_module = llvm.parse_assembly(str(module))

tm = llvm.Target.from_default_triple().create_target_machine()

with llvm.create_mcjit_compiler(llvm_module, tm) as ee:
    ee.finalize_object()
    print("===== ASSEMBLY")
    print(tm.emit_assembly(llvm_module))

    cfptr = ee.get_pointer_to_function(llvm_module.get_function('sum'))

    cfunc = CFUNCTYPE(c_int, c_int, c_int)(cfptr)

    res = cfunc(17,42)
    print("The result is", res)