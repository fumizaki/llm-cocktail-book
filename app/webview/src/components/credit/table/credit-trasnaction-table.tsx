import { cn } from "@/lib/style";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import type { CreditTransaction } from "@/domain/schema";
import { getAllAction } from "@/server-actions/credit-transaction/get-all";

type Props = {
	className?: string;
};

const headers = [
    'ID',
    'Type',
    'Credit',
    'Description'
]

export async function CreditTransactionTable({ className }: Props) {
	const state = await getAllAction();

	if (state.data.length <= 0) {
		return (
			<div className={cn("flex h-full", className)}>
				<p>データがありません</p>
			</div>
		);
	}
	return (
		<Table className={className}>
            <TableHeader>
                <TableRow>
                    {headers.map((v, idx) => {
                        return <TableHead key={idx}>{v}</TableHead>;
                    })}
                </TableRow>
            </TableHeader>
            <TableBody>
                {state.data.map((v: CreditTransaction, idx) => {
                    return (
                        <TableRow key={idx}>
                            <TableCell>{v.id}</TableCell>
                            <TableCell>{v.transactionType}</TableCell>
                            <TableCell>{v.credit}</TableCell>
                            <TableCell>{v.description}</TableCell>
                        </TableRow>
                    )
                })}
            </TableBody>
        </Table>
	);
}
