import {
	Dialog,
	DialogContent,
	DialogDescription,
	DialogHeader,
	DialogTitle,
	DialogTrigger,
} from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";
import { Pencil } from "lucide-react";
import { ChatbotIndex } from "@/domain/schema";

type Props = {
	value: ChatbotIndex;
};

export const EditChatbotIndexDialog = ({ value }: Props) => {
	return (
		<Dialog>
			<DialogTrigger asChild>
				<Button size={"icon"} variant={"ghost"}>
					<Pencil />
				</Button>
			</DialogTrigger>
			<DialogContent>
				<DialogHeader>
					<DialogTitle>Edit Chatbot Index?</DialogTitle>
					<DialogDescription>Edit {value.title}</DialogDescription>
					<div className={'h-80 overflow-auto'}>
						<p className={'whitespace-pre-wrap break-words'}>{value.content}</p>
					</div>
				</DialogHeader>
			</DialogContent>
		</Dialog>
	);
};
